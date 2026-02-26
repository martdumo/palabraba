# Palabraba ✨

Generador de imágenes aesthetic tipo diccionario con palabras y definiciones.

## Descripción

Palabraba es una herramienta que genera imágenes visuales atractivas con:
- Una palabra principal en tipografía grande
- Su definición con word-wrap automático
- Color de fondo aesthetic aleatorio (50 colores disponibles)
- Código hexadecimal del color utilizado
- Tipografía aleatoria del sistema (excluyendo fuentes de símbolos)

## Requisitos

- Python 3.8+
- Pillow (PIL)

## Instalación

```bash
pip install Pillow
```

## Uso

```bash
python palabraba.py
```

1. Ingresa la palabra que deseas mostrar
2. Ingresa la definición
3. La imagen se guardará automáticamente con timestamp

## Características

- 🎨 50 colores aesthetic (pasteles, muted, vaporwave, tierra)
- 🔤 Tipografías aleatorias del sistema
- 📐 Lienzo 1500x1500px
- ⚡ Contraste automático (texto blanco/negro según fondo)
- 📅 Nombre de archivo con timestamp para evitar sobrescritura

## Ejemplo de salida

```
✨ Bienvenido al Generador Aesthetic ✨
Ingresa la palabra: Serendipia
Ingresa la definición: Hallazgo afortunado e inesperado que se produce cuando se está buscando otra cosa distinta.

✅ ¡Imagen creada con éxito! Guardada como: aesthetic_20260226_143052.png
🎨 Color elegido: #FFB3BA
🔤 Tipografía usada: arial.ttf
```

## Licencia

MIT
