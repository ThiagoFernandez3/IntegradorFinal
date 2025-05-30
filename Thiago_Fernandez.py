from ClasesYLogica import CatalogoPeliculas , registroHora 

print('**Bienvenido a cuevana 2077 🎥**')
registroHora(f'Se inicio el programa.')

def ingresarCatalogo():
    
    while True:
        try:
            nombreCatalogo= input('Ingrese el nombre del catalogo de peliculas que desea ver.\n-').lower()
            if not nombreCatalogo.replace(" ", "").isalpha():
                raise ValueError
            else:
                return nombreCatalogo
            
        except(ValueError):
            print('Ingrese caracteres validos')
            continue
        
nombreCatalogo= ingresarCatalogo()

catalogo = CatalogoPeliculas(nombreCatalogo)

while True:
    try:
        print('\nQue desea hacer?')
        respuesta= int(input('1- Agregar peliculas al catalogo.\n2- Ver una lista con las peliculas en el catalogo.\n3- Eliminar catalogo.\n4- Cambiar catalogo.\n5- Ver registro.\n6-Salir\n-'))
        if respuesta not in (1,2,3,4,5,6):
            raise ValueError
        
        elif respuesta==1:
            catalogo.agregar_peliculas()
            
        elif respuesta== 2:
            catalogo.lista_peliculas()
            
        elif respuesta== 3:
            catalogo.eliminar_catalogo()
            
        elif respuesta== 4:
            nombreCatalogo= ingresarCatalogo()
            catalogo = CatalogoPeliculas(nombreCatalogo)
            
        elif respuesta== 5:
            catalogo.leer_registro()
            
        else:
            print('Adios👋')
            registroHora(f'Se cerro el programa.')
            break
            
    except(ValueError):
        print('Elija una opcion valida.')
        continue