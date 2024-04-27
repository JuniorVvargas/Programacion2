import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class TiendaOnline:
    def __init__(self, master):
        self.master = master
        self.master.title("Tienda Online")
        
        # Productos disponibles
        self.productos = {
            "Camiseta": 150,
            "Pantalón": 630,
            "Zapatos": 210,
            "Gorra": 96,
            "Bolso": 85,
            "Cartera": 963,
        }
        
        # Inicialización del carrito de compras
        self.carrito = {}
        
        # Crear widgets
        self.crear_widgets()

    def crear_widgets(self):
        # Etiqueta de bienvenida
        self.label_bienvenida = tk.Label(self.master, text="¡Bienvenido a la Tienda Libano", font=("Helvetica", 16))
        self.label_bienvenida.pack(pady=10)
        
        

        # Mostrar productos disponibles
        self.label_productos = tk.Label(self.master, text="Productos disponibles:", font=("Helvetica", 12))
        self.label_productos.pack(anchor="w", padx=10)

        self.lista_productos = tk.Listbox(self.master, selectmode="multiple", width=30, height=5)
        for producto in self.productos:
            self.lista_productos.insert(tk.END, f"{producto} - ${self.productos[producto]}")
        self.lista_productos.pack(padx=10)

        # Botón para agregar al carrito
        self.btn_agregar = tk.Button(self.master, text="Agregar al carrito", command=self.agregar_al_carrito)
        self.btn_agregar.pack(pady=10)

        # Carrito de compras
        self.label_carrito = tk.Label(self.master, text="Carrito de compras:", font=("Helvetica", 12))
        self.label_carrito.pack(anchor="w", padx=10)

        self.text_carrito = tk.Text(self.master, width=40, height=5)
        self.text_carrito.pack(padx=10)

        # Botón para finalizar compra
        self.btn_comprar = tk.Button(self.master, text="Finalizar compra", command=self.finalizar_compra)
        self.btn_comprar.pack(pady=10)

    def agregar_al_carrito(self):
        seleccionados = self.lista_productos.curselection()
        for indice in seleccionados:
            producto = self.lista_productos.get(indice).split(" - ")[0]
            precio = float(self.lista_productos.get(indice).split(" - ")[1].replace("$", ""))
            if producto in self.carrito:
                self.carrito[producto] += precio
            else:
                self.carrito[producto] = precio

        self.actualizar_carrito()

    def actualizar_carrito(self):
        self.text_carrito.delete("1.0", tk.END)
        total = 0
        for producto in self.carrito:
            self.text_carrito.insert(tk.END, f"{producto}: ${self.carrito[producto]}\n")
            total += self.carrito[producto]
        self.text_carrito.insert(tk.END, f"\nTotal: ${total}")

    def finalizar_compra(self):
        if not self.carrito:
            messagebox.showwarning("Error", "¡El carrito está vacío!")
            return

        total = sum(self.carrito.values())
        mensaje = f"¡Compra realizada!\nTotal a pagar: ${total:.2f}"
        messagebox.showinfo("Compra realizada", mensaje)
        self.carrito = {}
        self.actualizar_carrito()


def main():
    root = tk.Tk()
    app = TiendaOnline(root)
    root.mainloop()

if __name__ == "__main__":
    main()
