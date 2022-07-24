class Contact:
    def __init__(self, nombre, apellidos, edad, email, telef, casad, hijos, amigos, pelis):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.email = email
        self.telef = telef
        self.casad = casad
        self.hijos = hijos
        self.amigos = amigos
        self.pelis = pelis

shamu = Contact('Shamuel', 'Vargas Goddard', 20, 'shamuelvargas@gmail.com', '+507 6056-4530', False, False, ('Adrian', 'Juls'), {'1': 'Avatar', '2': 'Los Vengadores'})

for datos in shamu:
    print(datos)

