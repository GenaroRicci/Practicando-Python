import time
import math
import random
errormsg = 'Error: Debes introducir un numero valido.'
nm0msg = 'Introduce un numero mayor a 0'

###################################################################

total = 0
counter = 0
errormsg = " Error: Ingrese un número válido."

while True:
    value = input('Introduzca un número:\n')

    if value == 'fin':
        if counter > 0:
            media = total / counter
            print(f'El total es: {total:.2f}, la cantidad es: {counter} y el promedio es: {media:.2f}')
        else:
            print('No se ingresaron números válidos.')
        break

    try:
        total = total + float(value)
        counter = counter + 1
    except ValueError:
        print(errormsg)


##############################################

##############################################

















time.sleep(3)

