import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from ClasesYLogica import CatalogoPeliculas, registroHora
import os

class CatalogoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cuevana 2077 - Catálogo de Películas")
        self.catalogo = None

        self.label = tk.Label(root, text="Nombre del catálogo:")
        self.label.pack()

        self.entrada = tk.Entry(root)
        self.entrada.pack()

        self.btn_cargar = tk.Button(root, text="Crear/Cargar Catálogo", command=self.crear_catalogo)
        self.btn_cargar.pack(pady=5)

        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar Película", command=self.agregar_pelicula, state="disabled")
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_listar = tk.Button(self.frame_botones, text="Listar Películas", command=self.listar_peliculas, state="disabled")
        self.btn_listar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar Catálogo", command=self.eliminar_catalogo, state="disabled")
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        self.btn_registro = tk.Button(self.frame_botones, text="Ver Registro", command=self.ver_registro, state="disabled")
        self.btn_registro.grid(row=0, column=3, padx=5)

        self.resultado = scrolledtext.ScrolledText(root, width=60, height=15)
        self.resultado.pack(pady=10)

        registroHora("Se inició la interfaz gráfica.")

    def crear_catalogo(self):
        nombre = self.entrada.get().strip()
        if not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Nombre inválido. Solo letras.")
            return
        self.catalogo = CatalogoPeliculas(nombre)
        self.resultado.insert(tk.END, f"Catálogo '{nombre}' listo.\n")
        self.activar_botones()

    def activar_botones(self):
        self.btn_agregar.config(state="normal")
        self.btn_listar.config(state="normal")
        self.btn_eliminar.config(state="normal")
        self.btn_registro.config(state="normal")

    def agregar_pelicula(self):
        if not self.catalogo:
            return
        nombre = simpledialog.askstring("Agregar Película", "Nombre de la película:")
        if nombre:
            with open(self.catalogo.ruta_archivo, 'a') as archivo:
                archivo.write(nombre.strip().lower() + '\n')
            registroHora(f"Se agregó la película '{nombre}' al catálogo '{self.catalogo.nombre}'")
            self.resultado.insert(tk.END, f"Película '{nombre}' agregada.\n")

    def listar_peliculas(self):
        if not self.catalogo:
            return
        self.resultado.insert(tk.END, f"\n--- Catálogo '{self.catalogo.nombre}' ---\n")
        try:
            with open(self.catalogo.ruta_archivo, 'r') as archivo:
                peliculas = archivo.readlines()
                for p in peliculas:
                    self.resultado.insert(tk.END, f"• {p.strip()}\n")
            registroHora(f"Se listaron las películas del catálogo '{self.catalogo.nombre}'")
        except FileNotFoundError:
            messagebox.showerror("Error", "Catálogo no encontrado.")

    def eliminar_catalogo(self):
        if not self.catalogo:
            return
        confirm = messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar el catálogo?")
        if confirm:
            if os.path.exists(self.catalogo.ruta_archivo):
                os.remove(self.catalogo.ruta_archivo)
                registroHora(f"Se eliminó el catálogo '{self.catalogo.nombre}'")
                self.resultado.insert(tk.END, f"Catálogo '{self.catalogo.nombre}' eliminado.\n")

    def ver_registro(self):
        if not os.path.exists("registro.txt"):
            messagebox.showinfo("Registro", "Aún no hay registro de acciones.")
            return
        self.resultado.insert(tk.END, "\n--- Registro de acciones ---\n")
        with open("registro.txt", 'r') as archivo:
            for linea in archivo:
                self.resultado.insert(tk.END, linea)

if __name__ == "__main__":
    root = tk.Tk()
    app = CatalogoApp(root)
    root.mainloop()