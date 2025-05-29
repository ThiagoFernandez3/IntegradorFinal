from abc import ABC, abstractmethod

import os

from datetime import datetime

def registroHora(accion):
    hora= datetime.now().strftime('%Y-%m-%d %H:%M')
    with open('registro.txt', 'a') as registro:
        registro.write(f'-[{hora}] {accion}\n')

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
    
class CatalogoPeliculas(Peliculas):
    def __init__(self, nombreCatalogo):
        self.nombre = nombreCatalogo
        self.ruta_archivo = nombreCatalogo + '.txt'
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'w') as archivo:
                pass
            registroHora(f"Se creó el catálogo '{self.nombre}'")
        else:
            registroHora(f"Se cargó el catálogo existente '{self.nombre}'")
            
    def agregar_peliculas(self):
        pelicula= input(f'\nIngrese el nombre de la pelicula que quiere ingresar al catalogo{self.nombre}.\n-').lower()
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(pelicula+'\n')
        registroHora(f'Se agregó la película {pelicula} al catálogo {self.nombre}')
        print('\n-Pelicula agregada al catalogo ✅.')
    
    def lista_peliculas(self):
        registroHora(f'Se listaron las películas del catálogo {self.nombre}')
        print(f'\n-Lista del catalogo {self.nombre}:')
        with open(self.ruta_archivo, 'r') as archivo:
            for linea in archivo:
                print(f'•{linea.strip()}')
    
    def eliminar_catalogo(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            registroHora(f"Se eliminó el catálogo '{self.nombre}'")
            print(f'-EL Catalogo {self.nombre} ha sido eliminado.')
            
