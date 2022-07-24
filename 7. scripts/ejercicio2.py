import time

def main():
    timeTupl = time.localtime
    hora = timeTupl()[3] 
    minuto = timeTupl()[4]
    if (hora > 21):
        print('Ya es hora de salida :)')
    elif (hora < 11):
        print(f'Todavía no debes entrar')
    else: 
        print(f'La hora es {hora}:{minuto}')
        restHra = 21 - hora
        restMin = 60 - minuto
        print(f'Te quedan {restHra}:{restMin} horas de trabajo')

if __name__ == '__main__':
    main()