"""Inspecciona un video local y guarda una hoja de fotogramas si se solicita."""

import argparse
import json
import math
from pathlib import Path
import re
import subprocess


LOCAL_INPUT = ("-protocol_whitelist", "file,pipe")
PROBE_ENTRIES = (
    "format=duration:"
    "stream=index,codec_type,codec_name,width,height,avg_frame_rate,"
    "display_aspect_ratio,channels,duration:"
    "stream_disposition=attached_pic:stream_side_data=rotation"
)


def run(program, *arguments, data=None):
    try:
        result = subprocess.run([program, *arguments], input=data, capture_output=True)
    except FileNotFoundError as error:
        raise ValueError(f"No se encontró {program} en PATH.") from error
    if result.returncode:
        lines = result.stderr.decode("utf-8", errors="replace").strip().splitlines()
        details = "\n".join(lines[-4:])
        raise ValueError(f"{program} terminó con código {result.returncode}.\n{details}")
    return result


def positive_duration(metadata):
    try:
        duration = float(metadata.get("duration", 0))
    except (TypeError, ValueError):
        return None
    return duration if math.isfinite(duration) and duration > 0 else None


def probe(path):
    result = run(
        "ffprobe", "-v", "error", "-show_entries", PROBE_ENTRIES,
        "-of", "json", *LOCAL_INPUT, "-i", str(path),
    )
    metadata = json.loads(result.stdout)
    streams = metadata.get("streams", [])
    video = next(
        (stream for stream in streams if stream["codec_type"] == "video"
         and not stream.get("disposition", {}).get("attached_pic")),
        None,
    )
    if video is None:
        raise ValueError("El archivo no tiene una pista de video.")
    audio = [stream for stream in streams if stream["codec_type"] == "audio"]
    return video, audio, positive_duration(metadata.get("format", {}))


def audio_levels(path, stream):
    result = run(
        "ffmpeg", "-hide_banner", "-nostdin", "-nostats", "-v", "info", "-xerror",
        *LOCAL_INPUT, "-i", str(path), "-map", f"0:{stream['index']}",
        "-af", "volumedetect", "-f", "null", "-",
    )
    log = result.stderr.decode("utf-8", errors="replace")
    levels = re.findall(r"(mean_volume|max_volume):\s*(-?[0-9.]+) dB", log)
    return {
        "pista": stream["index"],
        **{name: float(value) for name, value in levels},
    }


def framesheet(path, destination, video, rotation, times):
    portrait = video["height"] > video["width"]
    if round(rotation / 90) % 2:
        portrait = video["width"] > video["height"]
    width, height = (288, 512) if portrait else (512, 288)
    scale = (
        f"scale=w='max(1,min({width},{height}*dar))':"
        f"h='max(1,min({height},{width}/dar))',setsar=1,"
        f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=0x171717"
    )
    frames = []
    sampled = []
    missing = []
    for second in times:
        result = run(
            "ffmpeg", "-v", "error", "-nostdin", "-xerror", "-ss", f"{second:.6f}",
            *LOCAL_INPUT, "-i", str(path), "-map", f"0:{video['index']}",
            "-vf", scale, "-frames:v", "1", "-threads:v", "1",
            "-pix_fmt", "rgb24", "-f", "rawvideo", "pipe:1",
        )
        if result.stdout:
            frames.append(result.stdout)
            sampled.append(second)
        else:
            missing.append(second)

    if not frames:
        raise ValueError("No se encontró un fotograma desde los segundos solicitados.")
    columns = min(3, len(frames))
    rows = (len(frames) + columns - 1) // columns
    result = run(
        "ffmpeg", "-v", "error", "-nostdin", "-f", "rawvideo",
        "-pixel_format", "rgb24", "-video_size", f"{width}x{height}", "-i", "pipe:0",
        "-vf", f"tile={columns}x{rows}:nb_frames={len(frames)}:padding=6:margin=6",
        "-frames:v", "1", "-threads:v", "1", "-c:v", "png", "-f", "image2pipe", "pipe:1",
        data=b"".join(frames),
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("xb") as output:
        output.write(result.stdout)
    return {
        "ruta": str(destination),
        "columnas": columns,
        "segundos": sampled,
        "sin_fotograma": missing,
    }


def nonnegative_seconds(value):
    seconds = float(value)
    if not math.isfinite(seconds) or seconds < 0:
        raise argparse.ArgumentTypeError("Usa segundos finitos, desde cero.")
    return seconds


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path, help="Ruta del video local.")
    parser.add_argument("--hoja", type=Path, help="Ruta nueva para la hoja PNG.")
    parser.add_argument("--segundos", type=nonnegative_seconds, nargs="+",
                        help="Marcas de la hoja, en segundos.")
    parser.add_argument("--medir-audio", action="store_true",
                        help="Mide nivel medio y pico de la primera pista de audio.")
    args = parser.parse_args()
    if args.segundos and not args.hoja:
        parser.error("--segundos requiere --hoja.")
    if args.hoja and args.hoja.suffix.lower() != ".png":
        parser.error("--hoja requiere una ruta con extensión .png.")

    try:
        source = args.video.resolve()
        if not source.is_file():
            raise ValueError(f"No se encontró el archivo {source}.")
        video, audio, total_duration = probe(source)
        video_duration = positive_duration(video)
        rotation = next(
            (item["rotation"] for item in video.get("side_data_list", []) if "rotation" in item),
            0,
        )
        report = {
            "archivo": str(source),
            "duracion_archivo_segundos": total_duration,
            "duracion_video_segundos": video_duration,
            "video": {key: video.get(key) for key in (
                "index", "codec_name", "width", "height", "avg_frame_rate", "display_aspect_ratio",
            )},
            "rotacion_video_grados": rotation,
            "audio": [{key: stream.get(key) for key in ("index", "codec_name", "channels")}
                      for stream in audio],
        }
        if args.medir_audio and audio:
            report["niveles_audio_dbfs"] = audio_levels(source, audio[0])
        if args.hoja:
            span = video_duration or total_duration
            times = args.segundos or (
                [round(span * portion, 6) for portion in (0, 0.1, 0.28, 0.52, 0.76, 0.94)]
                if span else [0]
            )
            report["hoja"] = framesheet(source, args.hoja.resolve(), video, rotation, times)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Error: {error}\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
