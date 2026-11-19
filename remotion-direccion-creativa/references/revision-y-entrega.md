# Revisión del montaje y del archivo final

## Haz una pasada con el montaje a la vista

Abre el tramo en Studio o en el archivo exportado y revísalo a velocidad real y al tamaño de destino cuando puedas. Para una edición puntual, compara con el mismo tramo del original e inspecciona los empalmes cercanos. Para una pieza nueva, recorre la apertura, la escena principal, los cambios de escena y el cierre. En redes, comprueba texto y acción al tamaño de un teléfono.

| Si observas esto | Ajusta esto |
| --- | --- |
| El inicio podría pertenecer a otro producto o relato. | Adelanta el gesto, el objeto o el resultado específico que presenta la idea. |
| Una interfaz o un dato pasa antes de poder entenderlo. | Acerca la parte que cambia y sostén su estado final. Ajusta el corte o el ritmo del texto. |
| El ojo se va al rótulo equivocado, se corta el texto o se tapa la acción. | Cambia jerarquía, encuadre o posición. Revisa los fotogramas donde los elementos coinciden y la zona que cubre la red. |
| Hay un negro involuntario, un salto, una fuente que aparece tarde o un efecto distinto en el exportado. | Comprueba los fotogramas a cada lado del corte, los límites de secuencia, las fuentes y las rutas de archivos. Vincula la animación a los fotogramas de Remotion. |
| El sonido llega fuera del gesto o la voz pierde claridad. | Compara el ataque con el fotograma de la acción y ajusta la música donde coincida con la voz. Comprueba otra vez la mezcla en ese tramo. |
| El cierre desaparece antes de que se lea el resultado o el siguiente paso. | Conserva el plano o la frase de cierre el tiempo necesario y comprueba su legibilidad en el último tramo. |

Corrige el problema de mayor impacto y vuelve a revisar el tramo ajustado y sus empalmes. Si cambió el archivo que vas a entregar, comprueba esa nueva versión.

## Comprueba un MP4 o un clip de referencia desde su ruta local

El script usa Python 3 y los ejecutables `ffprobe` y `ffmpeg` disponibles en el entorno. Desde la carpeta de la skill, pásale el video y una ruta nueva para la hoja de fotogramas.

```text
python scripts/revisar_video.py "ruta/video.mp4" --hoja "ruta/revision.png" --segundos 0.4 4.2 9.8 --medir-audio
```

- Sustituye los segundos de ejemplo por la apertura, los gestos, los cortes o el cierre del video. Con `--hoja` sin tiempos explícitos, el script busca seis muestras repartidas. Lee la hoja por filas, de izquierda a derecha, según las marcas solicitadas del informe. Para un empalme, toma muestras antes, durante y después.
- Sin `--hoja`, obtienes los datos técnicos. Comprueba dimensiones, FPS, duración y presencia de la pista acordada. Si activas `--medir-audio`, el informe añade el nivel medio y el pico de muestra de la primera pista. Para evaluar inteligibilidad y sincronía, reproduce el tramo cuando puedas. [Medición de volumen en FFmpeg](https://ffmpeg.org/ffmpeg-filters.html#volumedetect)
- Si falta alguna herramienta, usa la información de Studio, los fotogramas que puedas abrir y el reproductor disponible. Indica qué comprobaciones hiciste y cuáles quedaron pendientes.
