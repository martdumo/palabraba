import os
import random
import sys
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# Configurar UTF-8 para stdout en Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# 🎨 Graphic Design Automator: Lista de colores "aesthetic"
AESTHETIC_COLORS = [
    "#000000", "#001524", "#0057E7", "#005B96", "#006078",
    "#007872", "#008744", "#009688", "#00A0B0", "#00AEDB",
    "#00B159", "#011F4B", "#0274BD", "#03396C", "#0392CF",
    "#051E3E", "#0A162C", "#0E9AA7", "#0F0E11", "#137054",
    "#151C0D", "#174DB1", "#18363E", "#191308", "#1E1F26",
    "#20498A", "#23252D", "#251E3E", "#262842", "#27231E",
    "#272838", "#282D40", "#283655", "#28662B", "#292F36",
    "#293961", "#297EA1", "#29A8AB", "#2A4D69", "#2A8636",
    "#2AB7CA", "#2B1A12", "#2B2D35", "#2C497F", "#2D4030",
    "#2D5F6E", "#2E003E", "#2E1A78", "#2F6755", "#31393C",
    "#3385C6", "#343D46", "#35A79C", "#362FBB", "#36454F",
    "#3968CB", "#3A3C44", "#3A5253", "#3B5998", "#3B7DD8",
    "#3C2F2F", "#3D1E6D", "#3D2352", "#3D6FAD", "#3DA4AB",
    "#3E88A5", "#3E96F4", "#419E98", "#4279A3", "#434343",
    "#43AA47", "#44364B", "#445D48", "#44A9CC", "#451E3E",
    "#461E52", "#46484F", "#476C8A", "#49593C", "#49657B",
    "#49684C", "#4A495A", "#4A4E4D", "#4A88C5", "#4A91F2",
    "#4B1517", "#4B3832", "#4B86B4", "#4D648D", "#4F372D",
    "#4F3A35", "#4F5B66", "#50BCB9", "#510993", "#536872",
    "#536878", "#543622", "#54A7A2", "#54B2A9", "#55356E",
    "#556DC8", "#58545F", "#58668B", "#596854", "#5A2555",
    "#5D2A7B", "#5D7F61", "#5E1525", "#5E3023", "#5E5656",
    "#5F97AA", "#605E5F", "#63581F", "#63ACE5", "#6497B1",
    "#64A1F4", "#64CFF7", "#651E3E", "#65737E", "#65B8BF",
    "#65C3BA", "#66422D", "#674AB3", "#6B39BC", "#6B8E6E",
    "#6C1F9F", "#6D5B87", "#6E7F80", "#6F7C85", "#708090",
    "#712275", "#725444", "#75838D", "#75B9BF", "#76A787",
    "#76B4BD", "#7948A2", "#7998EE", "#7BC043", "#7C1715",
    "#7E7D7F", "#7E8D98", "#7F7129", "#7F803E", "#7F8E9E",
    "#800000", "#815355", "#816EC7", "#81B29A", "#81C953",
    "#828144", "#82BAC4", "#82C4BE", "#83828B", "#83D0C9",
    "#842D78", "#84C1FF", "#851E3E", "#854442", "#8569E4",
    "#8595A1", "#8874A3", "#8897BD", "#88A9B3", "#88AEDB",
    "#88D8B0", "#8B9DC3", "#8C9DA9", "#8D5524", "#8DBDFF",
    "#8E8E8E", "#8F7265", "#8F7A6E", "#8F8CF2", "#8FC9FF",
    "#9075D8", "#93C4D1", "#945C39", "#966045", "#96CEB4",
    "#975E64", "#97A2A6", "#97B299", "#97E589", "#989885",
    "#98A69A", "#9A8C98", "#9BF6FF", "#9E1C29", "#9F63C4",
    "#A063C8", "#A27CB8", "#A2D2FF", "#A348A6", "#A3CCD0",
    "#A41F13", "#A653F5", "#A68CEE", "#A6A6A6", "#A7ADBA",
    "#A86A24", "#A8E6CF", "#A97882", "#A9A8AA", "#AA3815",
    "#AA9D94", "#AAAAAA", "#AAABAE", "#AB2838", "#AC7E6E",
    "#ACAC9F", "#ACAEC5", "#AD794B", "#ADCBE3", "#ADD6FF",
    "#AFAFAF", "#AFCBD5", "#B0E1FF", "#B1AA81", "#B2336C",
    "#B26E4B", "#B3CDE0", "#B6C38D", "#B7DDDA", "#B84656",
    "#B8B8BC", "#B8DDDC", "#B9375E", "#BBADA1", "#BBBBBB",
    "#BBDAF2", "#BC4D1D", "#BCBCBC", "#BDE0FE", "#BDEAEE",
    "#BE8CE5", "#BE9A60", "#BE9B7B", "#BEFCFF", "#BF5F45",
    "#BF937C", "#BFAD8D", "#BFD6F6", "#C0C2CE", "#C0C5CE",
    "#C4AD9D", "#C56A1D", "#C6808C", "#C68642", "#C74F29",
    "#C7976F", "#C7AFF7", "#C99789", "#C9ADA7", "#CA7CD8",
    "#CAFFBF", "#CBDADB", "#CC2A36", "#CC9A52", "#CCC7BF",
    "#CCCCCC", "#CDB4DB", "#CEA2D7", "#CECBCB", "#CEDDBB",
    "#D0E1F9", "#D11141", "#D18623", "#D1D1D1", "#D1E8FC",
    "#D2C1B3", "#D2D4DC", "#D2E7FF", "#D36833", "#D3982F",
    "#D62D20", "#D6C9B0", "#D6CC99", "#D6EAFF", "#D6F5FF",
    "#D81334", "#D84F74", "#D8F7F2", "#D9B8AA", "#D9BDFF",
    "#DC6D18", "#DC8E90", "#DCD9CB", "#DCEDC1", "#DD517F",
    "#DDA6B9", "#DDDDDD", "#DEC3C3", "#DEFFFA", "#DF5F35",
    "#DF84E9", "#DFA290", "#DFE3EE", "#E07A5F", "#E0A899",
    "#E0AC69", "#E0DBD8", "#E19578", "#E1D8C3", "#E1DBD6",
    "#E2BAB1", "#E2E2E2", "#E37C78", "#E3826F", "#E3C9C9",
    "#E3DACA", "#E3E4FA", "#E3F0FF", "#E4A9A4", "#E4DCF1",
    "#E54AD3", "#E5989B", "#E5A836", "#E5E0E1", "#E5E6EB",
    "#E5F0FA", "#E68E36", "#E6C4B7", "#E6C6FF", "#E6E6EA",
    "#E7BB96", "#E7D3D3", "#E7D5C7", "#E7D7CB", "#E7EFF6",
    "#E8C539", "#E8EAEB", "#E8F3F2", "#E99E46", "#E9E2F3",
    "#E9E6DD", "#EA79A3", "#EAD5DC", "#EADBD6", "#EAF4FF",
    "#EB563A", "#EB6841", "#EBD2BC", "#EBF4F6", "#EC745C",
    "#ECF8FD", "#ED7D51", "#EDC951", "#EDEEEB", "#EDF6F9",
    "#EE4035", "#EE8EA5", "#EEC9D2", "#EEDBDB", "#EEE3E7",
    "#EEEEEE", "#EF9E84", "#EFA17F", "#EFA18A", "#EFBA97",
    "#F08D7E", "#F0E4E4", "#F0EBE3", "#F1C27D", "#F1CCBB",
    "#F1E1CE", "#F1E7EB", "#F2B418", "#F2E9E4", "#F2ECE1",
    "#F37735", "#F37736", "#F3B61F", "#F3D0D0", "#F4B6C2",
    "#F4B998", "#F4D44E", "#F4DED7", "#F4E7E7", "#F4F4F8",
    "#F57251", "#F5AD8C", "#F6ABB6", "#F6CD61", "#F7BAD3",
    "#F7DAE8", "#F7E752", "#F7EDE2", "#F7F7F7", "#F8CDA9",
    "#F8D8E4", "#F8E0C9", "#F8EDEB", "#F8F8FA", "#F8FBFF",
    "#F96868", "#F96CFF", "#F97698", "#F9CAA7", "#F9D671",
    "#F9F4F4", "#F9F6F2", "#FA92FB", "#FAD9C1", "#FAEBD7",
    "#FAEFED", "#FAF0E6", "#FAF5F1", "#FB8B24", "#FBF4EF",
    "#FBFDFB", "#FCDDD3", "#FCE4B4", "#FCE9DB", "#FD8E78",
    "#FDAC98", "#FDBD84", "#FDE5D4", "#FDF498", "#FDF5E6",
    "#FDF9F9", "#FDFBFB", "#FDFDFF", "#FDFFB6", "#FE4A49",
    "#FE7383", "#FE8A71", "#FE9C8F", "#FEB2A8", "#FEC8C1",
    "#FED766", "#FEFAE0", "#FF0000", "#FF3377", "#FF5588",
    "#FF5900", "#FF68A8", "#FF6F69", "#FF77AA", "#FF8B94",
    "#FF91B9", "#FF99CC", "#FFA700", "#FFAAA5", "#FFADAD",
    "#FFADCB", "#FFAFCC", "#FFB4A2", "#FFB600", "#FFB845",
    "#FFBBEE", "#FFC0B5", "#FFC425", "#FFC5A6", "#FFC8DD",
    "#FFCC5C", "#FFCDB2", "#FFD3B6", "#FFD4D1", "#FFD6A5",
    "#FFDAF5", "#FFDBAC", "#FFE0E9", "#FFE3D1", "#FFE9DC",
    "#FFEEAD", "#FFEFD7", "#FFF4E4", "#FFF4E6", "#FFF5C3",
    "#FFF5EE", "#FFF5F5", "#FFF6E9", "#FFFEF9", "#FFFFFF"
]

# 📝 Arrays para generar frases aleatorias
ARRAY1_SITUACIONAL = [
    "Che la heladeria de la plaza tiene un nuevo sabor a",
    "Me entere que para relajar la espalda es muy bueno tomarse un smoothie de",
    "No voy a poder ir al cumpleaños hoy, tengo un estudio intensivo sobre",
    "Te enteraste, salió una nueva Ley que regula a",
    "Viste la isla de Epstein? Parece que en una de las habitaciones encontraron a",
    "Parece que en las fosas comunes de Mejico encontraron un alien culeandose a",
    "Apartentemente no hace mas falta salir con carnet de conducir, ahora si te para la policia le tenes que mostrar",
    "Dicen que un travesti de los bosques de Palermo consiguió poderes magicos despues de franelear a",
    "El veganismo ya fue, ahora la posta es alimento a base de",
    "Uhh no sabes, en tinder me toco matchear con",
    "No importa cuanto salga, tan pronto cobre el aguinaldo me compro",
    "Sabes quien es Fanatico de Adrian Suar?",
    "Viste a quien eligieron para ser el nuevo tecladista de Rata Blanca? A",
    "Parece que el nuevo album de Charly Garcia se va a llamar",
    "Gracias a Milei bajo el precio de",
    "Mira el clarin dice que sin querer le hicieron una eutanacia a",
    "Aparentemente una Monja le partio el marote a",
    "Te enteraste? Parece que Ben Affleck va a hacer una pelicula sobre",
    "La sociedad esta muy mal, ayer me re cague a puteadas con",
    "Sabes con quien me cruse en la verduleria? Con",
    "Subi al 60 y el chofer era",
    "A que no sabes a quien me encontre cuando paseaba a mi pez por el verdin? A",
    "Mi vecino me enseño que la receta para que salga bien toda tarta de arvejas es agregarle",
    "Yo siempre que voy de camping me ataca",
    "A mi jefe le entro un virus en la computadora que hizo que le saliera de la disquetera",
    "Netflix ya fue la onda ahora es mirar",
    "El otro día escuchando spotify me salto una propaganda de",
    "Argentina no se recupera mas, ya fue... este año voto a",
    "El vino prestado y",
    "Dicen los libros de jurisprudencia que es bien sabido que todo abogado conoce",
    "Analizando esta ecuación surge de su aritmetica",
    "Ayer me opere y sabes lo que me sacaron del ombligo? A",
    "Parece que pixar va a sacar una pelicula sobre",
    "Si queres dejar de fumar tenes que tomar un te de"
]

ARRAY2_OBJETO = [
    "un sorete cosmico que cago",
    "una torre gemela que se cayo sobre",
    "la concha malolienta de",
    "el hijo abortado de",
    "una mermelada de",
    "un prepucio de",
    "el tratado de llambias que le robe a",
    "la enfermera que le suministraba risperidona a",
    "el Don Quijote reescrito por",
    "un Trabajo Practico deontologico sobre la cabeza de",
    "un pedo saxofonista de",
    "un helado de salame mal servido a",
    "la boleta de luz de",
    "un refresco con sabor a",
    "las uñas de",
    "una escultura de caca hecha por",
    "la causa de violencia intrafamiliar entre Mickey Mouse y",
    "una escena abstracta dirigida por David Lynch sobre",
    "el programa classico de los 90s, Video Match, pero dirigida por",
    "la escencia del ramal tigre del colectivo 60 hecha y refinada por",
    "una bola de mugre en la que estaba viviendo",
    "el perro del vecino afanandole un pan de la bolsa a",
    "un video de youtube sobre como hacer estofado de lengejas con",
    "un tractor en miniatura manejado por",
    "toda una la linea ferroviaria del tren Mitre exprimida por"
]

ARRAY3_SUJETO = [
    "Nestor Kirchner",
    "un enano haciendo malavares",
    "Lilo y Stitch en una fiesta de disfraces",
    "tu vieja",
    "el fiambre de Nisman",
    "un judio",
    "un musulman",
    "un ornitorrinco",
    "un lobotomizado fanatico de huracan",
    "un gordo mata chipa",
    "el Gordo Liverosky",
    "el mismisimo Peter de Polvorines",
    "el gordo de Space Jam",
    "el dolape de los tres chiflados",
    "Don Ramon enojado",
    "un mimo con una bicicleta en el ogt",
    "el payaso mas feo del Cirque du Soleil",
    "el sim que vino a fajarte por sacarle la escalera de la piscina",
    "Ace Ventura manejando mientras saca la sabiola por la ventanilla",
    "Arnold Schwarzenegger haciendo campaña por Rukauff",
    "Yoda haciendose una sopita knorr en el estacionamiento del DOT",
    "Carlos menem manejando el evangelion de asuka despues de robarselo y culpar  a los chinos",
    "Frondizi viajando en el tiempo para cumplir su sueño de vender saumerios",
    "Lopez Rega jugando a la UIJA con un salame a medio cortar",
    "Fito paez audienciando para trabajar en la octava temporada de Stranger Things",
    "el desodorante que habito a Marcelo Tinelli",
    "Johnny Bravo haciendose pasar por un crypto bro en el cumple de tu prima Juana",
    "Scooby Doo bajoneandose unas pitusas de limon con un fernandito",
    "Riquelme nervioso despues de que se le paso la mano armando el fuego para el asado"
]

# 🐍 Python Developer: Función para calcular contraste
def get_text_color(hex_color):
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    luminancia = 0.299 * r + 0.587 * g + 0.114 * b
    return "#000000" if luminancia > 140 else "#FFFFFF"

# 🎨 Mezclar dos colores de la paleta
def mix_colors(color1, color2, ratio=0.5):
    """Mezcla dos colores hex con un ratio dado (0-1)."""
    c1 = color1.lstrip('#')
    c2 = color2.lstrip('#')
    r1, g1, b1 = tuple(int(c1[i:i+2], 16) for i in (0, 2, 4))
    r2, g2, b2 = tuple(int(c2[i:i+2], 16) for i in (0, 2, 4))
    r = int(r1 * (1 - ratio) + r2 * ratio)
    g = int(g1 * (1 - ratio) + g2 * ratio)
    b = int(b1 * (1 - ratio) + b2 * ratio)
    return f"#{r:02x}{g:02x}{b:02x}"

# 🎲 Agregar efecto noise al fondo
def add_noise(image, noise_color_hex, intensity=15):
    """Agrega un efecto noise sutil a la imagen usando un color de la paleta."""
    noise_color = noise_color_hex.lstrip('#')
    r_n, g_n, b_n = tuple(int(noise_color[i:i+2], 16) for i in (0, 2, 4))
    
    pixels = image.load()
    width, height = image.size
    
    for y in range(height):
        for x in range(width):
            if random.random() < 0.08:  # 8% de probabilidad de noise por pixel
                r_orig, g_orig, b_orig = pixels[x, y]
                # Mezclar pixel original con color de noise
                blend = random.uniform(0.1, 0.3)
                r_new = int(r_orig * (1 - blend) + r_n * blend)
                g_new = int(g_orig * (1 - blend) + g_n * blend)
                b_new = int(b_orig * (1 - blend) + b_n * blend)
                pixels[x, y] = (r_new, g_new, b_new)
    
    return image

# 🏗️ Software Architect: Obtener fuente del sistema
def get_random_font():
    font_dir = "C:\\Windows\\Fonts"
    try:
        fonts = [f for f in os.listdir(font_dir) if f.lower().endswith('.ttf')]
        exclude = ['web', 'wing', 'symb', 'marlett', 'emoji', 'math', 'ding', 'holomdl2', 'segmdl2']
        valid_fonts = [f for f in fonts if not any(x in f.lower() for x in exclude)]
        chosen_font = random.choice(valid_fonts)
        return os.path.join(font_dir, chosen_font)
    except Exception as e:
        print(f"Error cargando fuentes: {e}. Usando fuente por defecto.")
        return None

# 🐍 Python Developer: Word Wrap
def wrap_text(text, font, max_width):
    lines = []
    words = text.split()
    while words:
        line = ''
        while words and font.getlength(line + words[0]) <= max_width:
            line = line + (words.pop(0) + ' ')
        lines.append(line.strip())
    return lines

# 🎲 Generar frase aleatoria
def generar_frase():
    parte1 = random.choice(ARRAY1_SITUACIONAL)
    parte2 = random.choice(ARRAY2_OBJETO)
    parte3 = random.choice(ARRAY3_SUJETO)
    return f"{parte1} {parte2} {parte3}."

def crear_imagen(frase, bg_color, noise_color=None):
    """Crea una imagen con la frase y el color de fondo especificado."""
    text_color = get_text_color(bg_color)

    # 2. Configuración de lienzo (1500 x 1500)
    width, height = 1500, 1500
    img = Image.new("RGB", (width, height), bg_color)
    
    # Agregar efecto noise si se proporciona un color
    if noise_color:
        img = add_noise(img, noise_color)
    
    draw = ImageDraw.Draw(img)

    # 3. Configuración de tipografía
    font_path = get_random_font()
    try:
        font_principal = ImageFont.truetype(font_path, 80)
        font_hex = ImageFont.truetype(font_path, 40)
    except:
        font_principal = ImageFont.load_default()
        font_hex = ImageFont.load_default()

    # 4. Cálculo de posiciones y diseño
    margin = 150
    max_text_width = width - (margin * 2)

    # Procesar frase con word wrap
    frase_lines = wrap_text(frase, font_principal, max_text_width)

    # Calcular altura total del bloque de texto
    line_spacing = 30
    bbox_sample = draw.textbbox((0, 0), frase_lines[0] if frase_lines else "", font=font_principal)
    single_line_height = bbox_sample[3] - bbox_sample[1]
    total_text_height = (single_line_height * len(frase_lines)) + (line_spacing * (len(frase_lines) - 1))

    # Centrar verticalmente
    start_y = (height - total_text_height) // 2

    # Dibujar la frase línea por línea
    current_y = start_y
    for line in frase_lines:
        draw.text((margin, current_y), line, font=font_principal, fill=text_color)
        current_y += single_line_height + line_spacing

    # Dibujar el código Hexadecimal
    hex_text = f"Hex: {bg_color}"
    bbox_hex = draw.textbbox((0, 0), hex_text, font=font_hex)
    hex_width = bbox_hex[2] - bbox_hex[0]
    hex_height = bbox_hex[3] - bbox_hex[1]

    hex_x = width - hex_width - 80
    hex_y = height - hex_height - 80

    draw.text((hex_x, hex_y), hex_text, font=font_hex, fill=text_color)

    # 5. Exportar imagen
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"frase_{timestamp}.png"

    img.save(filename, quality=100)
    return filename, bg_color, font_path, noise_color

def main():
    print("✨ Generador de Frases Aleatorias ✨\n")

    while True:
        # Generar frase automáticamente
        frase = generar_frase()
        print(f"📝 Frase generada:\n{frase}\n")

        # Mostrar menú de opciones
        print("Selecciona una opción:")
        print("  1. Imprimir la frase en una imagen")
        print("  2. Generar otra frase")
        print("  3. Salir")
        print("  4. Imprimir frase personalizada")

        opcion = input("\nOpción: ").strip()

        if opcion == "1":
            # Mezclar dos colores aleatorios de la paleta para el fondo
            color1 = random.choice(AESTHETIC_COLORS)
            color2 = random.choice(AESTHETIC_COLORS)
            ratio = random.uniform(0.3, 0.7)  # Ratio aleatorio para la mezcla
            bg_color = mix_colors(color1, color2, ratio)
            
            # Elegir otro color para el efecto noise
            noise_color = random.choice(AESTHETIC_COLORS)
            
            filename, color, font_path, noise = crear_imagen(frase, bg_color, noise_color)
            print(f"\n✅ ¡Imagen creada con éxito! Guardada como: {filename}")
            print(f"🎨 Colores mezclados: {color1} + {color2} (ratio: {ratio:.2f})")
            print(f"🎨 Color de fondo resultante: {color}")
            print(f"✨ Color de noise: {noise}")
            print(f"🔤 Tipografía usada: {os.path.basename(font_path) if font_path else 'Default'}\n")
            break
        elif opcion == "2":
            print("\n" + "="*50 + "\n")
            continue
        elif opcion == "3":
            print("\n👋 ¡Hasta luego!")
            break
        elif opcion == "4":
            # Opción para frase personalizada
            print("\n✍️  Ingresa tu frase personalizada:")
            frase_personalizada = input("> ").strip()
            
            if frase_personalizada:
                # Mezclar dos colores aleatorios de la paleta para el fondo
                color1 = random.choice(AESTHETIC_COLORS)
                color2 = random.choice(AESTHETIC_COLORS)
                ratio = random.uniform(0.3, 0.7)
                bg_color = mix_colors(color1, color2, ratio)
                
                # Elegir otro color para el efecto noise
                noise_color = random.choice(AESTHETIC_COLORS)
                
                filename, color, font_path, noise = crear_imagen(frase_personalizada, bg_color, noise_color)
                print(f"\n✅ ¡Imagen creada con éxito! Guardada como: {filename}")
                print(f"🎨 Colores mezclados: {color1} + {color2} (ratio: {ratio:.2f})")
                print(f"🎨 Color de fondo resultante: {color}")
                print(f"✨ Color de noise: {noise}")
                print(f"🔤 Tipografía usada: {os.path.basename(font_path) if font_path else 'Default'}\n")
            else:
                print("\n❌ Frase vacía. Inténtalo de nuevo.\n")
        else:
            print("\n❌ Opción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()
