# Handoff - Palabraba

## Estado del Proyecto

✅ **Completado** - Versión 1.0 funcional

## Archivos del Proyecto

| Archivo | Descripción |
|---------|-------------|
| `palabraba.py` | Script principal del generador |
| `.gitignore` | Ignorar caché, venv, imágenes generadas |
| `README.md` | Documentación para usuarios |
| `blueprint.md` | Arquitectura y diseño técnico |
| `handoff.md` | Este documento |

## Configuración del Entorno

### Windows

```bash
# Instalar dependencia
pip install Pillow

# Ejecutar
python palabraba.py
```

### Linux/Mac

```bash
# Instalar dependencia
pip install Pillow

# Ejecutar
python3 palabraba.py
```

## Notas Técnicas

1. **Fuentes**: El script usa fuentes del sistema (`C:\Windows\Fonts`). En Linux/Mac modificar `get_random_font()` para usar `/usr/share/fonts` o `/Library/Fonts`.

2. **UTF-8**: Configurado `sys.stdout.reconfigure(encoding='utf-8')` para soportar emojis en consola Windows.

3. **Contraste**: Fórmula de luminancia relativa (0.299R + 0.587G + 0.114B) con threshold 140.

## Próximas Mejoras (Opcional)

- [ ] Soporte para fuentes personalizadas
- [ ] Interfaz gráfica (Tkinter/PyQt)
- [ ] Modo batch (procesar CSV)
- [ ] Exportar a otros formatos (JPG, WebP)
- [ ] Paletas de colores personalizables
- [ ] Opción de elegir color manualmente

## Repositorio

- **Remote**: https://github.com/martdumo/palabraba.git
- **Branch**: master

## Contacto

Desarrollado por @martdumo
