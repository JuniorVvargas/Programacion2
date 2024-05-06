import tkinter as tk

def ingresar():
    pass

ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("800x500") 

frame_izquierda = tk.Frame(ventana, width=200, height=400, bg="royal Blue")
frame_izquierda.pack(side="left", fill="both", expand=True)

frame_derecha = tk.Frame(ventana, width=200, height=400, bg="lightgray")
frame_derecha.pack(side="right", fill="both", expand=True)

logo_label = tk.Label(frame_izquierda, text="Volleyball Store", font=("CALIBRI", 16), bg="royal Blue")
logo_label.pack(pady=20)
logo = tk.PhotoImage(file="C:\Users\carlo\Desktop\python\Diccionarios\logo.png") 
logo_label = tk.Label(frame_izquierda, image=logo)
logo_label.pack(pady=20)

titulo_label = tk.Label(frame_derecha, text="Inicio de Sesión", font=("Arial", 18))
titulo_label.pack(pady=20)

usuario_label = tk.Label(frame_derecha, text="Usuario:", font=("Arial", 12))
usuario_label.pack()

usuario_entry = tk.Entry(frame_derecha, font=("Arial", 12))
usuario_entry.pack()

clave_label = tk.Label(frame_derecha, text="Contraseña:", font=("Arial", 12))
clave_label.pack()

clave_entry = tk.Entry(frame_derecha, show="*", font=("Arial", 12)) 
clave_entry.pack()

boton_ingresar = tk.Button(frame_derecha, text="Ingresar", command=ingresar, font=("Arial", 12))
boton_ingresar.pack(pady=20)

ventana.mainloop()