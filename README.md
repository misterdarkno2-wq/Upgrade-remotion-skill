# Mejora de videos en Remotion

`$remotion-direccion-creativa` es una skill para Codex que ayuda a crear, editar y revisar videos en Remotion. Convierte el material del proyecto en decisiones concretas de encuadre, montaje y sonido. En una composición existente, localiza el problema en un plano o fotograma y compara el tramo original con el editado en Remotion Studio cuando está disponible.

## Qué puedes hacer con la skill

- Darle al video una apertura basada en un gesto, una pregunta o un detalle propio del tema.
- Ajustar los cortes a lo que ocurre en pantalla y dar tiempo para leer el texto o reconocer el resultado de una acción.
- Corregir saltos de animación, texto cortado y problemas de sincronía entre imagen y sonido.
- Pedir una revisión con observaciones por momento o aplicar los ajustes directamente en el proyecto.

## Instalar en Codex

Pega este mensaje en un chat de Codex.

```text
Usa $skill-installer para instalar la skill de https://github.com/misterdarkno2-wq/Upgrade-remotion-skill/tree/main/remotion-direccion-creativa
```

Abre tu proyecto de Remotion en Codex e invoca la skill con `$remotion-direccion-creativa`. Para hacer cambios y comprobarlos en Studio, Codex necesita acceso al proyecto.

## Ejemplo de uso

> Usa `$remotion-direccion-creativa` para pulir esta demo vertical. Revisa todos los videos de mi carpeta de referencias y usa las técnicas que encajen. Conserva el guion aprobado, haz que los cortes sigan las acciones y comprueba en Studio que se vea bien el resultado de cada interacción.

Indica la ruta de tu carpeta de referencias en el mensaje. La skill revisa cada video reproducible cuando le pides usar todos. Puedes consultar cómo aprovecha las grabaciones de producto, la tipografía animada y los ejemplos con presentador en la [guía de referencias](remotion-direccion-creativa/references/referencias-de-estilo.md).

## Usar en ChatGPT

Si tu cuenta tiene Skills habilitadas, descarga el repositorio, comprime la carpeta `remotion-direccion-creativa` en un ZIP y cárgalo desde **Plugins → Skills → Crear → Subir desde tu computadora**. [Ayuda de ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

Si puedes editar un GPT personalizado, pega el cuerpo de `SKILL.md` en el campo **Instrucciones**. [Ver instrucciones de la skill](remotion-direccion-creativa/SKILL.md)
