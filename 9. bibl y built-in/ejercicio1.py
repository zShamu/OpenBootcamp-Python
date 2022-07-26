paises = input('Ingrese una lista de países (separados por comas): ')
#Se convierte a lista
paises = paises.split(',')
#Se eliminan duplicados
paises = set(paises)
#Se ordena
paises = tuple(paises)
print(paises)