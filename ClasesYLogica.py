#Importo las bibliotecas necesarias.
from abc import ABC, abstractmethod
import os
from datetime import datetime

#Defino dos excepciones personalizadas para mas adelante.
class PeliculaYaAgregada(Exception):
    pass

class ListaVacia(Exception):
    pass

#Defino una funcion "registroHora" que usa datetime para guardar cada accion en un archivo ".txt".
def registroHora(accion):
    hora= datetime.now().strftime('%Y-%m-%d %H:%M')
    with open('registro.txt', 'a') as registro:
        registro.write(f'-[{hora}] {accion}\n')

#Creo la clase Peliculas con sus metodos abstractos y el atributo privado "self.__nombre".

class Peliculas(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre 
    def __str__(self):
        return self.__nombre
    
    @abstractmethod
    def agregar_peliculas(self):
        pass

    @abstractmethod
    def lista_peliculas(self):
        pass

    @abstractmethod
    def eliminar_catalogo(self):
        pass
    
    @abstractmethod
    def leer_registro(self):
        pass

#La clase hija "CatalogoPeliculas" y se definen los atributos necesarios de ruta archivo y nombre.
class CatalogoPeliculas(Peliculas):
    def __init__(self, nombreCatalogo):
        self.nombre = nombreCatalogo
        self.ruta_archivo = nombreCatalogo + '.txt'
        
#En caso de que el catalogo ingresado exista se abre y en el caso contrario se crea,
#en cada caso se guarda la accion en "regristro.txt".

        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'w') as archivo:
                pass
            registroHora(f'Se creo el catalogo {self.nombre}')
        else:
            registroHora(f'Se cargo el catalogo existente {self.nombre}')
            
#La funcion guarda en el catalogo las peliculas que ingrese el usuario 
    def agregar_peliculas(self):
        while True:
            try:
                pelicula= input(f'\nIngrese el nombre de la pelicula que quiere ingresar al catalogo {self.nombre}.\n-').lower()
                with open(self.ruta_archivo, 'r') as catalogo:
                    for linea in catalogo:
                        if pelicula == linea:
                            raise(PeliculaYaAgregada)
                        else:
                            with open(self.ruta_archivo, 'a') as archivo:
                                archivo.write(pelicula+'\n')
                            registroHora(f'Se agrego la película {pelicula} al catálogo {self.nombre}')
                            print('\n-Pelicula agregada al catalogo ✅.')
                            break
                        
#Salta un mensaje en caso de que la pelicula ya este en el catalogo               
            except(PeliculaYaAgregada):
                print('La pelicula ya esta en el catalogo, intente agregar una diferente')
                continue


#La funcion muestra por la terminal las peliculas almacenadas en el catalogo actual.         
    def lista_peliculas(self):
        registroHora(f'Se listaron las peliculas del catalogo {self.nombre}')
        print(f'\n-Lista del catalogo {self.nombre}:')
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                for linea in archivo:
                    if linea== '' or ' ':
                        raise(ListaVacia)
                    else:
                        print(f'•{linea.strip()}')
                        
#Salta un mensaje en caso de que el catalogo este vacio.
        except(ListaVacia):
            print(f'-Catalogo vacio, intenta agregar una pelicula.')
            
#La funcion elimina el archivo ".txt" que contenga el catalogo actual.  
    def eliminar_catalogo(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            registroHora(f'Se elimino el catalogo {self.nombre}')
            print(f'-EL Catalogo {self.nombre} ha sido eliminado.')
            
#Simplemente muestra las acciones guardadas en "registro.txt".

    def leer_registro(self):
        registroHora(f'Se abrio el registro.')
        print('\n-Registro de acciones:')
        with open('registro.txt', 'r') as registro:
            for linea in registro:
                print(linea)
            
