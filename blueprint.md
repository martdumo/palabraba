# Blueprint - Palabraba

## Arquitectura del Sistema

```
palabraba.py
├── Imports (os, random, sys, textwrap, datetime, PIL)
├── AESTHETIC_COLORS (lista de 50 colores hex)
├── Funciones
│   ├── get_text_color(hex_color) → calcula contraste
│   ├── get_random_font() → selecciona fuente del sistema
│   ├── wrap_text(text, font, max_width) → word wrap
│   └── main() → punto de entrada
└── Exportación PNG con timestamp
```

## Flujo de Ejecución

1. **Input**: Usuario ingresa palabra y definición
2. **Configuración**: 
   - Color de fondo aleatorio de 50 opciones aesthetic
   - Cálculo de color de texto (blanco/negro por contraste)
3. **Renderizado**:
   - Lienzo 1500x1500px
   - Tipografía aleatoria (excluyendo símbolos)
   - Word-wrap para definición
   - Centrado vertical del bloque de texto
4. **Exportación**: PNG con timestamp `aesthetic_YYYYMMDD_HHMMSS.png`

## Componentes

| Componente | Responsabilidad |
|------------|----------------|
| `get_text_color()` | Fórmula de luminancia relativa para contraste WCAG |
| `get_random_font()` | Listar fuentes Windows, filtrar símbolos/matemáticas |
| `wrap_text()` | Separar texto en líneas según ancho máximo |
| `main()` | Orquestar input, renderizado y exportación |

## Dependencias

| Librería | Versión | Propósito |
|----------|---------|-----------|
| Pillow | ≥8.0 | Manipulación de imágenes |

## Paleta de Colores

- Pasteles clásicos (5)
- Rosas y cálidos (10)
- Verdes y naturaleza (10)
- Azules y fríos (10)
- Morados y vaporwave (10)
- Neutros y Nude (5)

## Especificaciones Técnicas

- **Canvas**: 1500x1500px RGB
- **Margen**: 150px laterales, 80px esquina inferior
- **Tipografías**: 
  - Palabra: 140pt
  - Definición: 65pt
  - Hex: 40pt
- **Espaciado**: 20px entre líneas de definición, 80px entre secciones
