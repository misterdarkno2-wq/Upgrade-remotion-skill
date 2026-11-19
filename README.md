# Mejora de videos en Remotion

`remotion-direccion-creativa` es una skill para Codex y Claude que ayuda a crear, editar y revisar videos en Remotion. Convierte el material del proyecto en decisiones concretas de encuadre, montaje y sonido. En una composición existente, localiza el problema en un plano o fotograma y compara el tramo original con el editado en Remotion Studio cuando está disponible.

## Qué puedes hacer con la skill

- Darle al video una apertura basada en un gesto, una pregunta o un detalle propio del tema.
- Ajustar los cortes a lo que ocurre en pantalla y dar tiempo para leer el texto o reconocer el resultado de una acción.
- Corregir saltos de animación, texto cortado y problemas de sincronía entre imagen y sonido.
- Pedir una revisión con observaciones por momento o aplicar los ajustes directamente en el proyecto.
- Adaptar la edición a la red elegida y recibir títulos y texto de publicación después del video final.

## Instalar en Codex

Pega este mensaje en un chat de Codex.

```text
Usa $skill-installer para instalar la skill de https://github.com/misterdarkno2-wq/Upgrade-remotion-skill/tree/main/remotion-direccion-creativa
```

Abre tu proyecto de Remotion en Codex e invoca la skill con `$remotion-direccion-creativa`. Para hacer cambios y comprobarlos en Studio, Codex necesita acceso al proyecto.

## Instalar en Claude

**Claude Code.** Copia la carpeta `remotion-direccion-creativa` a `.claude/skills/` dentro de tu proyecto. Para usarla en todos tus proyectos locales, cópiala a `~/.claude/skills/`. Abre Claude Code desde tu proyecto de Remotion y usa `/remotion-direccion-creativa`. [Guía de Claude Code](https://code.claude.com/docs/en/skills#choose-where-skills-load)

**Claude web.** Verifica que esté habilitada la ejecución de código. Comprime la carpeta `remotion-direccion-creativa` para que sea la carpeta raíz del ZIP. En Claude, ve a **Customize → Skills**, pulsa **+** y selecciona **Create skill → Upload a skill**. Activa la skill y menciona su nombre al pedir una revisión. Para aplicar cambios o comprobarlos en Studio, el entorno necesita acceso al proyecto de Remotion. [Ayuda de Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Ejemplo de uso

> Usa la skill remotion-direccion-creativa para pulir esta demo vertical. Revisa todos los videos de mi carpeta de referencias y usa las técnicas que encajen. Conserva el guion aprobado, haz que los cortes sigan las acciones y comprueba en Studio que se vea bien el resultado de cada interacción.

Indica la ruta de tu carpeta de referencias en el mensaje. La skill revisa cada video reproducible cuando le pides usar todos. Puedes consultar cómo aprovecha las grabaciones de producto, la tipografía animada y los ejemplos con presentador en la [guía de referencias](remotion-direccion-creativa/references/referencias-de-estilo.md).

Si estás preparando un video para redes, la skill te pregunta por el destino, el público o el objetivo cuando esos datos faltan y afectan la edición. Con el video final recibirás un título recomendado, dos alternativas y un texto listo para publicar. [Guía de edición y publicación](remotion-direccion-creativa/references/publicacion-en-redes.md)

## Usar tus efectos de sonido

Indica las carpetas de tu biblioteca y las acciones que quieres enfatizar. La skill puede buscar en las subcarpetas con un script de Python, preseleccionar efectos y colocarlos en la línea de tiempo. Los paquetes de la skill contienen la guía y el buscador. Dale al entorno de edición acceso a tus archivos de audio. [Guía de efectos de sonido](remotion-direccion-creativa/references/efectos-de-sonido.md)

## Usar en ChatGPT

Si tu cuenta tiene Skills habilitadas, descarga el repositorio, comprime la carpeta `remotion-direccion-creativa` en un ZIP y cárgalo desde **Plugins → Skills → Crear → Subir desde tu computadora**. [Ayuda de ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

Si puedes editar un GPT personalizado, pega el cuerpo de `SKILL.md` en el campo **Instrucciones**. [Ver instrucciones de la skill](remotion-direccion-creativa/SKILL.md)
