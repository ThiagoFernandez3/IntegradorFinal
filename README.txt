README.txt

# Catálogo de Películas - Cuevana 2077 🎥

Este proyecto en Python permite crear y gestionar un catálogo de películas de forma interactiva desde la terminal.
El sistema está dividido en dos archivos:

---

## Archivos

### 1. `ClasesYLogica.py`

Contiene la lógica de negocio implementada mediante Programación Orientada a Objetos (POO).

- Define una clase abstracta `Peliculas` con métodos que deben ser implementados:
  - `agregar_peliculas()`
  - `lista_peliculas()`
  - `eliminar_catalogo()`
- La clase `CatalogoPeliculas` hereda de `Peliculas` e implementa estos métodos:
  - **Agregar películas**: Añade títulos ingresados por el usuario a un archivo `.txt`.
  - **Listar películas**: Muestra todas las películas en el catálogo.
  - **Eliminar catálogo**: Borra el archivo del catálogo.
- La funcion ´registroHora´ guarda en un archivo ´.txt´ la hora y la accion realizado.
---

### 2. `Thiago_Fernandez.py`

Archivo principal que ejecuta el programa.

- Solicita al usuario un nombre para el catálogo (se usará como nombre de archivo).
- Muestra un menú con las siguientes opciones:
  1. Agregar películas al catálogo.
  2. Ver la lista de películas en el catálogo.
  3. Eliminar el catálogo.
  4. Salir del programa.
- Valida entradas del usuario y maneja errores comunes como caracteres no válidos o elecciones fuera de rango.

---

## Cómo ejecutar

1. Asegúrate de tener Python 3 instalado.
2. Ejecuta el archivo `Thiago_Fernandez.py`.
3. Sigue las instrucciones en pantalla.

---

## Notas

- Los catálogos se guardan como archivos `.txt` en el mismo directorio del script.
- El nombre del catálogo no debe incluir números ni caracteres especiales.
- Se recomienda ejecutar ambos archivos en el mismo directorio para evitar errores de importación.---

## Versión con Interfaz Gráfica

Si prefieres una experiencia visual, prueba el archivo `Catalogo_Interfaz.py`, que ofrece la misma funcionalidad en una ventana interactiva usando la librería Tkinter.
