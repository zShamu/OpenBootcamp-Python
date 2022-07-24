numero = int(input("Introduce un numero: "))

def esPrimo(numero: int):
    if numero == 4:
        return False
    elif numero == 0 or numero == 1:
        return True
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True

if esPrimo(numero):
	print("Es primo")
else:
	print("No es primo")