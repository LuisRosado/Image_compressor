import tkinter as tk
from tkinter import Label, Button
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image
import os

# Función para abrir la imagen
def open_image():
    file_path = askopenfilename()
    if file_path:
        img = Image.open(file_path)
        myWidth, myHeight = img.size
        img = img.resize((myWidth, myHeight), Image.LANCZOS)

        save_path = generate_output_filename(file_path)
        img.save(save_path)
        if save_path:
            label_status.config(text="Imagen guardada con éxito", font=('Arial Bold', 18))

        return img

# Función para generar el nombre del archivo de salida
def generate_output_filename(input_path):
    directory, filename = os.path.split(input_path)
    name, ext = os.path.splitext(filename)
    output_filename = f"{name}_compressed.jpg"
    return os.path.join(directory, output_filename)


# Función para manejar el flujo
def compress_image():
    open_image()



# Crear la ventana principal
root = tk.Tk()
root.title("Compresor de Imágenes")
root.iconbitmap("compresion.ico")
root.geometry("400x200")
root.resizable(False,False)


button_compress = Button(root, width= 25, height= 2, bg='white',font=('Arial Bold',18) , text="Seleccionar y comprimir imagen", command=compress_image)
button_compress.pack(pady=10)

label_status = Label(root, text="")
label_status.pack(pady=10)

# Ejecutar la ventana
root.mainloop()
