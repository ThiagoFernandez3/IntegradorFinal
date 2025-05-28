from ClasesYLogica import CatalogoPeliculas

print('**Bienvenido a cuevana 2077 🎥**')
while True:
    try:
        nombreCatalogo= input('Ingrese el nombre del catalogo de peliculas que desea ver.\n-').lower()
        if not nombreCatalogo.replace(" ", "").isalpha():
            raise ValueError
        else:
            break
        
    except(ValueError):
        print('Ingrese caracteres validos')
        continue
    
catalogo = CatalogoPeliculas(nombreCatalogo)

while True:
    try:
        print('\nQue desea hacer?')
        respuesta= int(input('1- Agregar peliculas al catalogo.\n2- Ver una lista con las peliculas en el catalogo.\n3- Eliminar catalogo.\n4- Salir\n-'))
        if respuesta not in (1,2,3,4):
            raise ValueError
        
        elif respuesta==1:
            catalogo.agregar_peliculas()
            
        elif respuesta== 2:
            catalogo.lista_peliculas()
            
        elif respuesta== 3:
            catalogo.eliminar_catalogo()
            
        else:
            print('Adios👋')
            break
            
    except(ValueError):
        print('Elija una opcion valida.')
        continue