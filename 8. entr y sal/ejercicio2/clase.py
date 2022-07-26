import json

class Vehiculo():
    def __init__(self, marca, modelo, anio) -> None:
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

fav = Vehiculo('Nissan', '350z', '2008')

ruta = './8. entr y sal/ejercicio2/cargaobjeto.txt'
archivo = open(ruta, 'a+')
archivo.write(f'Marca: {fav.marca} \nModelo: {fav.modelo} \nAño: {fav.anio}')