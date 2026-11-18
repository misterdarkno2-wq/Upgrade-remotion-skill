# Efectos de sonido en Remotion

## Busca para una acción concreta

Localiza las carpetas que indique el usuario. La colección inicial incluye `450 cinematic sound effects` para botones, clics, interfaz, transiciones y golpes, `336 SFX` para ambientes, elementos, whooshes y risers, y `230 mixed sound effcts` para clips de reacción y otros sonidos variados. Usa las bibliotecas que estén accesibles en el proyecto o en el entorno de trabajo.

Desde la carpeta de la skill, pasa cada biblioteca al buscador. Sin términos, el comando cuenta los archivos encontrados por formato. Con términos, busca en los nombres de archivos y subcarpetas y ordena primero las rutas con más coincidencias.

```text
python scripts/buscar_sfx.py --carpeta "ruta/a/450 cinematic sound effects" --carpeta "ruta/a/336 SFX" --carpeta "ruta/a/230 mixed sound effcts" click button hud
```

Busca por la función que debe cumplir el sonido. Prueba `click button hud` para un toque o confirmación, `whoosh swoosh swish` para un desplazamiento, y `riser impact hit` para preparar o marcar un cambio de escena. Los nombres sirven para preseleccionar. Escucha candidatos en el pasaje del video cuando el entorno lo permita y elige por ataque, duración y tono. Los MP4 del banco son candidatos de audio si tienen una pista utilizable.

## Coloca y revisa

- Pon el ataque de un clic o impacto en el fotograma del gesto o de la llegada visual. Para un riser, haz que su punto culminante llegue al cambio de escena. Deja espacio entre efectos cuando varios gestos ocurren seguidos.
- Copia al proyecto los fragmentos que uses y sigue su forma de cargar y temporizar audio. Si el proyecto usa `public/` y `staticFile()`, guarda ahí los efectos elegidos con nombres claros.
- Reproduce el tramo con voz, música y efectos juntos. Ajusta el nivel y la duración donde compitan, escucha las colas cerca de cada corte y comprueba la sincronía a velocidad real. Si el entorno no permite escuchar la mezcla, indica qué momentos quedan por revisar.
