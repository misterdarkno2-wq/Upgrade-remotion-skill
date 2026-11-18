"""Busca efectos por nombre y subcarpeta en bibliotecas locales."""

import argparse
from collections import Counter
from pathlib import Path
import re
import unicodedata


FORMATS = {".aac", ".aif", ".aiff", ".flac", ".m4a", ".mp3", ".mp4", ".ogg", ".opus", ".wav"}


def words(text):
    normalized = unicodedata.normalize("NFKD", text.casefold())
    normalized = "".join(character for character in normalized if not unicodedata.combining(character))
    return set(re.findall(r"[^\W\d_]+", normalized))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--carpeta", action="append", required=True, type=Path,
                        help="Biblioteca que se recorre en forma recursiva. Se puede repetir.")
    parser.add_argument("--limite", type=int, default=20, help="Cantidad máxima de coincidencias.")
    parser.add_argument("terminos", nargs="*", help="Palabras que pueden aparecer en la ruta.")
    args = parser.parse_args()
    if args.limite < 1:
        parser.error("--limite debe ser mayor que cero")

    roots = dict.fromkeys(folder.resolve() for folder in args.carpeta)
    terms = words(" ".join(args.terminos))
    variants = [{term, term + "s", term + "es", term + "ing"} for term in terms]
    matches = {}
    for root in roots:
        if not root.is_dir():
            parser.error(f"No se encontró la carpeta: {root}")
        counts = Counter()
        for file in root.rglob("*"):
            extension = file.suffix.casefold()
            if extension not in FORMATS or not file.is_file():
                continue
            counts[extension] += 1
            if variants:
                path_words = words(file.relative_to(root).as_posix())
                score = sum(bool(forms & path_words) for forms in variants)
                if score:
                    matches[file] = max(score, matches.get(file, 0))
        formats = ", ".join(f"{extension}: {counts[extension]}" for extension in sorted(counts))
        print(f"{root.name}: {sum(counts.values())} archivos ({formats})")

    if terms:
        print(f"Coincidencias: {len(matches)}")
        ordered = sorted(matches, key=lambda file: (-matches[file], str(file).casefold()))
        for file in ordered[:args.limite]:
            print(file)


if __name__ == "__main__":
    main()
