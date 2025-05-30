==============================
 PROYECTO: Catálogo de Películas
==============================

🎯 DESCRIPCIÓN
---------------
Este programa permite gestionar un catálogo de películas con una interfaz gráfica construida con Tkinter.
 Se pueden crear catálogos, agregar películas, listarlas, eliminarlas y ver un historial de acciones.

🧩 FUNCIONALIDADES
-------------------
- Crear o cargar un catálogo .txt ingresando su nombre.
- Agregar películas al catálogo.
- Ver la lista de películas agregadas.
- Eliminar el catálogo completo.
- Ver el historial de acciones con fecha y hora.

📁 ESTRUCTURA DE ARCHIVOS
---------------------------
- `ClasesYLogica.py`: contiene la lógica principal (clases y funciones).
- `Thiago_Fernandez.py`: versión por consola.
- `interfaz.py`: interfaz gráfica con botones y vista de registros.
- `registro.txt`: archivo generado automáticamente que guarda cada acción con hora.

📌 REGISTRO DE ACCIONES
-------------------------
Cada vez que se realiza una acción, se guarda en el archivo `registro.txt` con formato:
    [YYYY-MM-DD HH:MM] Descripción de la acción

✅ EJEMPLO DE REGISTRO:
    [2025-05-28 18:33] Se creó el catálogo 'peliculas'
    [2025-05-28 18:34] Se agregó la película 'matrix' al catálogo 'peliculas'

▶️ EJECUCIÓN DEL PROGRAMA
---------------------------
Para la interfaz gráfica:

Catalogo_Interfaz.py

Para la versión por consola:

Thiago_Fernandez.py

✍️ AUTOR
---------
Thiago Fernández
