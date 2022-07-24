class Vehiculo:
    def __init__(self, color, ruedas, puertas) -> None:
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada) -> None:
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


corolita = Coche('Gris', 4, 4, '240Km/h', '2600cc')

print(f'El Corolita\nColor: {corolita.color}\nRuedas: {corolita.ruedas}\nPuertas: {corolita.puertas}\nVelocidad: {corolita.velocidad}\nCilindrada: {corolita.cilindrada}')
