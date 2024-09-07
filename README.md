# Compresor de Imágenes

Este es un simple programa de compresión de imágenes creado con Python y la biblioteca Tkinter. Permite a los usuarios seleccionar una imagen desde su sistema, comprimirla, y guardarla con un nombre modificado en el mismo directorio.


## Requisitos

- Python 3.x
- Biblioteca Pillow (`PIL`) para manipulación de imágenes
- Tkinter (incluido en la mayoría de las instalaciones de Python)


## Instalación

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Instala la biblioteca Pillow si no la tienes ya:
  pip install pillow


## Uso

Ejecuta el script.
  python compresor_imagenes.py
  
Se abrirá una ventana de interfaz gráfica con un botón "Seleccionar y comprimir imagen". Haz clic en este botón para seleccionar una imagen desde tu sistema.
La imagen seleccionada será redimensionada y guardada en el mismo directorio con un sufijo _compressed en el nombre del archivo.


## Funcionalidades


Abrir Imagen: Selecciona una imagen desde el explorador de archivos.
Comprimir Imagen: La imagen seleccionada se redimensionará y guardará con un nuevo nombre en el mismo directorio.


## Nota


El programa guarda la imagen en formato JPEG, independientemente del formato original.


## Contribuciones


Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar tus pull requests.
