anio = int(input("Introduce un año: "))

def esBisiesto(anio: int):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

print(esBisiesto(anio))