from abc import ABC, abstractmethod

import os

class Peliculas(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self._nombre = nombre + '.txt'
        
    def agregar_peliculas(self):
        pass
    
    def lista_peliculas(self):
        pass
        
    def eliminar_catalogo(self):
        pass
    
class Catalogo_Peliculas(Peliculas):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def agregar_peliculas(self):
        with open(self._nombre, 'a') as archivo:
            archivo.write(input('Ingrese el nombre de la pelicula que quiere ingresar al catalogo\n-')+'\n').lower()
            print('-Pelicula agregada al catalogo')
    
    def lista_peliculas(self):
        print(f'-Lista del catalogo {self._nombre}:')
        with open(self._nombre, 'r') as archivo:
            for linea in archivo:
                print(f'•{linea.strip()}')
    
    def eliminar_catalogo(self):
        if os.path.exists(self._nombre):
            os.remove(self._nombre)
            print(f'-EL Catalogo {self._nombre} ha sido eliminado.')
            
print('Bienvenido a cuevana 2077 🎥')
while True:
    try:
        nombreCatalogo= input('Ingrese el nombre del catalogo de peliculas que desea ver.\n-').lower().strip()
        if not nombreCatalogo.replace(" ", "").isalpha():
            raise ValueError
        else:
            break
        
    except(ValueError):
        print('Ingrese caracteres validos')
        continue
    
catalogo = Catalogo_Peliculas(nombreCatalogo)

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