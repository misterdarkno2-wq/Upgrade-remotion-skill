---
name: remotion-direccion-creativa
description: Crea, edita o revisa videos en Remotion. Adapta referencias de estilo, efectos visuales como carrusel, órbita y cristal, y bibliotecas de sonido. Ajusta el montaje para Reels, TikTok, YouTube y otras redes. Después de entregar el video, propone títulos y texto para publicarlo.
---

# Mejora de videos en Remotion

Convierte el propósito, el público y el material de cada video en decisiones de guion, montaje y puesta en pantalla. Para implementar o previsualizar la composición, usa los comandos y convenciones del proyecto y las guías de Remotion que tengas disponibles.

## Define el destino

Si vas a crear un video y falta el destino, pregunta dónde se verá. Para crear o adaptar una pieza para redes, usa la [guía de edición y publicación](references/publicacion-en-redes.md). Pregunta solo por los datos pendientes que cambian el montaje o la entrega. En revisiones y correcciones puntuales, parte del formato existente.

## Parte de la composición actual

Si hay una pieza previa, reproduce el tramo afectado y ubica el plano, gesto o fotograma donde se pierde claridad, naturalidad o sincronía. Usa ese momento como referencia para comprobar la mejora. En una edición puntual, limita la intervención al problema pedido. Conserva el guion, los recursos de marca y el formato que el usuario haya fijado.

## Encuentra el punto de vista

- En Codex, procesa las referencias de video y sonido desde su ruta local. Devuelve al chat fotogramas, tiempos y mediciones de FFmpeg. Evita devolver pistas o fragmentos como entrada de audio al modelo (por ejemplo, mediante `audio(...)`), porque eso puede bloquear el chat con «Audio input is not available». Para entender palabras, usa subtítulos o una transcripción local si están disponibles. Si faltan, avanza con lo observable e indica qué parte del diálogo queda por confirmar. Puedes conservar, mezclar y exportar la pista original en Remotion.
- Revisa el material y las referencias antes de definir el diseño. Extrae rasgos observables que sirvan al encargo, como el momento del corte, la distancia de cámara, el uso del sonido ambiente o la relación entre texto e imagen. Adáptalos al contenido y a la identidad del usuario.
- Si el usuario entrega una carpeta de referencias o pide aplicar los patrones de su colección, usa la [guía de referencias de estilo](references/referencias-de-estilo.md). Cuando pida usar todos los videos, revisa cada archivo reproducible y elige las técnicas que encajen con el encargo.
- Si el usuario menciona `efectosparareplicar.mp4`, pide un efecto de ese catálogo o usa `/efectos` en su mensaje, consulta la [guía de los 19 efectos visuales](references/efectos-visuales.md). Aplica los que pida sobre el material de destino. Si pide una muestra de todos, dales tramos propios para que pueda revisar cada movimiento.
- Elige qué debe entender, sentir o poder hacer el público al final. Construye el comienzo alrededor de un gesto, una frase, una imagen o una pregunta que pertenezca a ese tema. Si al cambiar de producto, personaje o historia el inicio funciona igual, busca un detalle más propio en el material.

## Monta alrededor de lo que ocurre

- Ordena las escenas según lo que cambia para el espectador. Da prioridad a la grabación, demostración, objeto o detalle que permite ver ese cambio. En un video solo de gráficos, encuentra ese detalle en los datos, el lenguaje o la forma de representarlos.
- Decide el corte al ver la acción o escuchar la frase. Corta en el gesto, el cambio de idea o la reacción cuando eso aclare el relato. Sostén los planos que requieren lectura y deja tiempo para reconocer el resultado antes de avanzar. Usa música, silencios y sonido ambiente según lo que esté sucediendo.
- Haz que cada momento tenga un foco visible. Usa tipografía, encuadre y movimiento para dirigir la mirada hacia él. Reserva tarjetas, degradados, rebotes y transiciones elaboradas para los momentos donde aporten jerarquía, continuidad o un tono que el encargo pida.
- Si escribes locución, léela en voz alta y ajusta las frases al registro del público. Sustituye promesas vagas por acciones o detalles comprobables. Haz que el texto editorial aporte contexto o guíe la mirada. Si hay subtítulos, sincronízalos con las frases y revisa que se lean sin tapar lo importante.

## Corrige el acabado en Remotion

- Si hay un salto, un hueco o un corte a destiempo, inspecciona el tramo fotograma a fotograma. Comprueba los límites de las secuencias y el FPS de la composición. Si una animación depende del reloj del navegador, ajústala a los fotogramas de la composición para que responda al mover el cursor de Studio.
- Si un texto se corta, una capa tapa la acción o un recurso aparece tarde, revisa el encuadre al tamaño de destino, el orden de capas y el primer fotograma que usa la fuente o el medio afectado.
- Si una acción y su sonido llegan en momentos distintos, alinea sus entradas en la línea de tiempo. Si cuesta entender la voz, ajusta la música en el pasaje donde coinciden y escucha de nuevo la mezcla.
- Si el usuario aporta una biblioteca de efectos o pide diseño sonoro, consulta la [guía de efectos de sonido](references/efectos-de-sonido.md) para buscar candidatos, colocarlos y revisar la mezcla.

## Comprueba la mejora

Si el encargo incluye edición, corrige primero el problema de mayor impacto. Compara el tramo original y el ajustado en Studio a velocidad real y al tamaño de destino cuando sea posible. Si cambiaste tiempos, comprueba los empalmes cercanos y la duración final. En un video nuevo, prioriza la apertura, el momento que demuestra la idea y el cierre. Si solo te piden revisar, señala momentos concretos y el ajuste que propones. Si falta una previsualización funcional, comprueba lo posible con los recursos, los fotogramas o la línea de tiempo disponibles e indica qué quedó pendiente.

En una entrega para redes, enlaza primero el video final verificado. Después incluye los títulos y el texto de publicación adaptados a cada destino.
