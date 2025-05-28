from abc import ABC, abstractmethod
import os

class Peliculas(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre 
    def __str__(self):
        return self.__nombre
    
    @abstractmethod
    def agregar_pelicula(self):
        pass

    @abstractmethod
    def listar_peliculas(self):
        pass

    @abstractmethod
    def eliminar_peliculas(self):
        pass
    
class CatalogoPeliculas(Peliculas):
    def __init__(self, nombreCatalogo):
        self.nombre = nombreCatalogo
        self.ruta_archivo = nombreCatalogo + '.txt'
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'w') as archivo:
                pass
            
    def agregar_peliculas(self):
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(input('Ingrese el nombre de la pelicula que quiere ingresar al catalogo\n-').lower()+'\n')
            print('-Pelicula agregada al catalogo')
    
    def lista_peliculas(self):
        print(f'-Lista del catalogo {self.nombre}:')
        with open(self.ruta_archivo, 'r') as archivo:
            for linea in archivo:
                print(f'•{linea.strip()}')
    
    def eliminar_catalogo(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(f'-EL Catalogo {self.nombre} ha sido eliminado.')
            
