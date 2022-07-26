from functools import reduce

def suma_impares(numeros: list):
    impares = filter(es_impar, numeros)
    suma = reduce(lambda a, b: a+b, impares)
    return suma

def es_impar(x: int):
    if x % 2 == 0:
        return False
    else:
        return True
