class Alumno:
    def __init__(self, nombre, nota) -> None:
        self.nombre = nombre
        self.nota = float(nota)

    def datos(cls):
        print(f'Nombre del estudiante: {cls.nombre}')
        print(f'Nota del estudiante: {cls.nota}')

    def aprobado(cls):
        if (cls.nota > 61):
            print('Ha aprobado')
        else:
            print('No ha aprobado')

shamu = Alumno('Shamuel Vargas', 88.88)
shamu.datos()
shamu.aprobado()
