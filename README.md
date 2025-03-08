# Filtrado de Historias de Instagram

Este proyecto es un script en Python que automatiza el proceso de extracción de archivos de imágenes y videos desde una exportación de datos de Instagram. Instagram exporta estos datos organizándolos en muchas carpetas, una por cada día en el que subiste historias. Dentro de estas carpetas se encuentran tanto los archivos multimedia como otros archivos que no nos interesa conservar.

Esta herramienta permite automatizar el proceso de extracción de imágenes y videos, moviéndolos a una sola carpeta centralizada para facilitar su acceso y organización.

## Requisitos

- Python 3.x

## Instalación

1. Clonar o descargar este repositorio.
2. Asegurar que tienes Python instalado en tu sistema.

## Uso

1. Modifica la variable `ruta_exportacion` en el script `filter_instagram_stories.py` con la ruta donde has descargado los datos de Instagram.
2. Ejecuta el script con el siguiente comando:

   ```bash
   python filter_instagram_stories.py
   ```
3. Los archivos filtrados se encontrarán en una nueva carpeta llamada `Instagram_Stories_filtered` dentro del directorio de exportación.

## Funcionalidades

- Recorre de manera recursiva todas las subcarpetas en busca de archivos multimedia.
- Mueve archivos `.jpg` y `.mp4` a un solo directorio organizado.

## Notas

- Asegúrate de proporcionar la ruta correcta de la carpeta descargada desde Instagram.
- No se eliminan los archivos originales, solo se mueven a una nueva ubicación.

