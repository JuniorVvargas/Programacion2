import tkinter as tk
from tkinter import messagebox

def registrar():
    mensaje = f"""
    Nombre: {entry_nombre.get()}
    Apellido: {entry_apellido.get()}
    Edad: {entry_edad.get()}
    Dirección: {entry_direccion.get()}
    Teléfono: {entry_telefono.get()}
    Sexo: {var_sexo.get()}
    Ciudad: {listbox_ciudad.get(tk.ACTIVE)}
    """
    messagebox.showinfo("Información Registrada", mensaje)

ventana = tk.Tk()
ventana.title("Formulario de Registro")

campos = ["Nombre", "Apellido", "Edad", "Dirección", "Teléfono"]
for i, campo in enumerate(campos):
    tk.Label(ventana, text=campo + ":").grid(row=i, column=0, sticky="e")
    tk.Entry(ventana).grid(row=i, column=1)

var_sexo = tk.StringVar(value="Masculino")
tk.Radiobutton(ventana, text="Masculino", variable=var_sexo, value="Masculino").grid(row=i+1, column=1, sticky="w")
tk.Radiobutton(ventana, text="Femenino", variable=var_sexo, value="Femenino").grid(row=i+2, column=1, sticky="w")

ciudades = ["Cartagena", "Medellin", "Barranquilla"]
listbox_ciudad = tk.Listbox(ventana, selectmode=tk.SINGLE, height=len(ciudades))
for ciudad in ciudades: listbox_ciudad.insert(tk.END, ciudad)
listbox_ciudad.grid(row=i+3, column=1)

tk.Button(ventana, text="Registrar", command=registrar).grid(row=i+4, columnspan=2)
ventana.mainloop()
