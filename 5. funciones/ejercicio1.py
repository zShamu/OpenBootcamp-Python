import math

#Area de un Triangulo
h = input('Inserte la altura del triangulo: ')
b = input('Inserte la base del triangulo: ')

a = (1/2) * float(h) * float(b)

print(f'El area del triangulo es: {a}')


#Area de un Circulo
r = input('Inserte el radio del circulo: ')

aC = math.pi * pow(r, 2)
aC = round(aC, 2)

print(f'El area del circulo es: {aC}')