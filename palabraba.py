import os
import random
import textwrap
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# 🎨 Graphic Design Automator: Lista de 50 colores "aesthetic" (Pasteles, Muted, Vaporwave, Tierra, etc.)
AESTHETIC_COLORS =[
    "#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF", # Pasteles clásicos
    # Rosas y cálidos
    "#F49E9E", "#F4B2B0", "#F2C2C2", "#F0D1D1", "#EAD3D3",
    "#D8A499", "#E2B8B2", "#EAC8C1", "#F1DCD6", "#F9EBE8",
    # Verdes y naturaleza
    "#A8E6CF", "#DCEDC1", "#FFD3B6", "#FFAAA5", "#FF8B94",
    "#8B9A8B", "#A4B4A4", "#BCCDBC", "#D3E3D3", "#EAF6EA",
    # Azules y fríos
    "#A1C9F1", "#B2D2F2", "#C3DBF4", "#D5E5F6", "#E6EEF8",
    "#6D9DC5", "#8EAFD1", "#AEC1DE", "#CFD4EA", "#EFE8F6",
    # Morados y vaporwave
    "#CBAACB", "#ABDEE6", "#FFFFB5", "#FFCCB6", "#F3B0C3",
    "#B0A8B9", "#C3B9CB", "#D6CADD", "#EAE0F0", "#FDF5FF",
    # Neutros y Nude
    "#D5D6EA", "#F6F6EB", "#D7ECD9", "#F5D5CB", "#F6E6E4",
    "#CDB4DB", "#FFC8DD", "#FFAFCC", "#BDE0FE", "#A2D2FF"
]

# 🐍 Python Developer: Función para calcular contraste (letras blancas o negras según el fondo)
def get_text_color(hex_color):
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    # Fórmula de luminancia relativa
    luminancia = 0.299 * r + 0.587 * g + 0.114 * b
    return "#000000" if luminancia > 140 else "#FFFFFF"

# 🏗️ Software Architect: Obtener fuente del sistema evitando símbolos
def get_random_font():
    font_dir = "C:\\Windows\\Fonts"
    try:
        # Filtramos solo fuentes TrueType
        fonts =[f for f in os.listdir(font_dir) if f.lower().endswith('.ttf')]
        # Filtro de seguridad para excluir fuentes de símbolos o matemáticas
        exclude =['web', 'wing', 'symb', 'marlett', 'emoji', 'math', 'ding', 'holomdl2', 'segmdl2']
        valid_fonts =[f for f in fonts if not any(x in f.lower() for x in exclude)]
        
        chosen_font = random.choice(valid_fonts)
        return os.path.join(font_dir, chosen_font)
    except Exception as e:
        print(f"Error cargando fuentes: {e}. Usando fuente por defecto.")
        return None

# 🐍 Python Developer: Lógica para separar texto en líneas (Word Wrap)
def wrap_text(text, font, max_width):
    lines =[]
    words = text.split()
    while words:
        line = ''
        # Mientras haya palabras y el ancho de la línea sea menor al máximo
        while words and font.getlength(line + words[0]) <= max_width:
            line = line + (words.pop(0) + ' ')
        lines.append(line.strip())
    return lines

def main():
    print("✨ Bienvenido al Generador Aesthetic ✨")
    palabra = input("Ingresa la palabra: ")
    definicion = input("Ingresa la definición: ")

    # 1. Configuración de colores
    bg_color = random.choice(AESTHETIC_COLORS)
    text_color = get_text_color(bg_color)

    # 2. Configuración de lienzo (1500 x 1500)
    width, height = 1500, 1500
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # 3. Configuración de tipografía
    font_path = get_random_font()
    try:
        font_word = ImageFont.truetype(font_path, 140)  # Palabra grande
        font_def = ImageFont.truetype(font_path, 65)    # Definición mediana
        font_hex = ImageFont.truetype(font_path, 40)    # Hex chico
    except:
        font_word = ImageFont.load_default()
        font_def = ImageFont.load_default()
        font_hex = ImageFont.load_default()

    # 4. Cálculo de posiciones y diseño (Graphic Design Automator 🎨)
    margin = 150
    max_text_width = width - (margin * 2)

    # Calcular altura total del bloque para centrarlo verticalmente
    # Altura de la palabra
    bbox_word = draw.textbbox((0, 0), palabra, font=font_word)
    word_height = bbox_word[3] - bbox_word[1]

    # Procesar definición (Word Wrap)
    def_lines = wrap_text(definicion, font_def, max_text_width)
    
    # Calcular altura de la definición
    line_spacing = 20
    def_height = 0
    if def_lines:
        bbox_def_sample = draw.textbbox((0, 0), def_lines[0], font=font_def)
        single_line_height = bbox_def_sample[3] - bbox_def_sample[1]
        def_height = (single_line_height * len(def_lines)) + (line_spacing * (len(def_lines) - 1))

    # Altura total (Palabra + Espacio grande + Definición)
    space_between_sections = 80
    total_block_height = word_height + space_between_sections + def_height

    # Punto de inicio (Y) para que todo quede centrado en el eje Y, pero alineado a la izquierda en X
    start_y = (height - total_block_height) // 2

    # Dibujar la Palabra
    draw.text((margin, start_y), palabra, font=font_word, fill=text_color)

    # Dibujar la Definición
    current_y = start_y + word_height + space_between_sections
    for line in def_lines:
        draw.text((margin, current_y), line, font=font_def, fill=text_color)
        current_y += single_line_height + line_spacing

    # Dibujar el código Hexadecimal (Abajo, esquina inferior derecha)
    hex_text = f"Hex: {bg_color}"
    bbox_hex = draw.textbbox((0, 0), hex_text, font=font_hex)
    hex_width = bbox_hex[2] - bbox_hex[0]
    hex_height = bbox_hex[3] - bbox_hex[1]
    
    # Margen especial de 80px desde la esquina para el hex
    hex_x = width - hex_width - 80
    hex_y = height - hex_height - 80
    
    draw.text((hex_x, hex_y), hex_text, font=font_hex, fill=text_color)

    # 5. Exportar imagen (Software Architect 🏗️)
    # Formato de fecha para que nunca se sobreescriba: AñoMesDia_HoraMinutoSegundo
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"aesthetic_{timestamp}.png"
    
    img.save(filename, quality=100)
    print(f"\n✅ ¡Imagen creada con éxito! Guardada como: {filename}")
    print(f"🎨 Color elegido: {bg_color}")
    print(f"🔤 Tipografía usada: {os.path.basename(font_path) if font_path else 'Default'}")

if __name__ == "__main__":
    main()
