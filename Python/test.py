import time
import math
import random
errormsg = 'Error: Debes introducir un numero valido.'
nm0msg = 'Introduce un numero mayor a 0'

###################################################################

print('Escribe tu lista de numeros separados por una coma (,):')

listain = input('>')

lista1 = []

#float(n.strip()) for n in lista1.split(',')
#max = None
#min = None

for n in listain.split(','):
    try:
        numero = float(n.strip())
        lista1.append(numero)
    except ValueError:
        print(f'{errormsg} Valor ignorado: "{n.strip()}"')

if lista1:
    maximo = max(lista1)
    minimo = min(lista1)
    print(f'Su mayor numero es {maximo} y su menor numero es {minimo}')
else:
    print('No hay numeros validos')


##############################################

##############################################

time.sleep(3)

