import tkinter as tk
from tkinter import messagebox, simpledialog
from ClasesYLogica import CatalogoPeliculas

class CatalogoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cuevana 2077 - Catálogo de Películas")
        self.catalogo = None

        self.label = tk.Label(root, text="Ingrese el nombre del catálogo:")
        self.label.pack(pady=5)

        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack(pady=5)

        self.btn_iniciar = tk.Button(root, text="Iniciar Catálogo", command=self.iniciar_catalogo)
        self.btn_iniciar.pack(pady=5)

        self.frame_opciones = tk.Frame(root)

    def iniciar_catalogo(self):
        nombre = self.entry_nombre.get().strip().lower()
        if not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Ingrese un nombre válido para el catálogo.")
            return

        self.catalogo = CatalogoPeliculas(nombre)
        self.label.config(text=f"Catálogo: {nombre}")
        self.entry_nombre.pack_forget()
        self.btn_iniciar.pack_forget()

        self.frame_opciones.pack(pady=10)
        tk.Button(self.frame_opciones, text="Agregar Película", command=self.agregar_pelicula).pack(fill='x')
        tk.Button(self.frame_opciones, text="Ver Lista", command=self.ver_lista).pack(fill='x')
        tk.Button(self.frame_opciones, text="Eliminar Catálogo", command=self.eliminar_catalogo).pack(fill='x')
        tk.Button(self.frame_opciones, text="Salir", command=self.root.quit).pack(fill='x')

    def agregar_pelicula(self):
        pelicula = simpledialog.askstring("Agregar Película", "Nombre de la película:")
        if pelicula:
            with open(self.catalogo.ruta_archivo, 'a') as archivo:
                archivo.write(pelicula.strip().lower() + '\n')
            messagebox.showinfo("Éxito", "Película agregada al catálogo.")

    def ver_lista(self):
        try:
            with open(self.catalogo.ruta_archivo, 'r') as archivo:
                peliculas = archivo.readlines()
            lista = "\n".join([f"- {p.strip()}" for p in peliculas])
            messagebox.showinfo("Lista de Películas", lista if lista else "Catálogo vacío.")
        except FileNotFoundError:
            messagebox.showerror("Error", "El catálogo no existe.")

    def eliminar_catalogo(self):
        confirm = messagebox.askyesno("Eliminar", "¿Estás seguro de eliminar el catálogo?")
        if confirm:
            self.catalogo.eliminar_catalogo()
            messagebox.showinfo("Eliminado", "Catálogo eliminado.")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = CatalogoApp(root)
    root.mainloop()
