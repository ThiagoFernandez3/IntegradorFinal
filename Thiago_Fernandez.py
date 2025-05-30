#Importo los modulos necesarios de ClasesYLogica
from ClasesYLogica import CatalogoPeliculas , registroHora 

print('**Bienvenido a cuevana 2077 🎥**')
registroHora(f'Se inicio el programa.')

#Creo una funcion que regresa el nombre que tendra el catalogo y analiza que sea valido con ".isalpha()" (Solo acepta letras),
#mientras que ".replace()" cambia cada espacio en lo que ingrese el usuario por nada

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
        
#Guardo el nombre de la funcion anterior en una variable y luego instancio "CatalogoPeliculas" con esa variable.     
  
nombreCatalogo= ingresarCatalogo()
catalogo = CatalogoPeliculas(nombreCatalogo)

#Muestro por terminal las opciones disposibles y en cada caso llamo los metodos necesarios,
#en caso de que el usuario ingrese algo que no este en las opciones se repite.
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