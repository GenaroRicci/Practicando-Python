import time
import math
import random
errormsg = 'Error: Debes introducir un numero valido.'
nm0msg = 'Introduce un numero mayor a 0'

###################################################
try:
    manejador_archivo = open('mbox.txt')
    counter_lineas = 0
    for linea in manejador_archivo:
        linea = linea.rstrip()#Elimina todos los espacios en blanco a la derecha de una cadenas
        if linea.startswith('From:'):
            counter_lineas = counter_lineas + 1
            print(linea)
    print(f'El total de lineas de redactores es: {counter_lineas}')
except FileNotFoundError:
    print('No se pudo acceder al archivo')
#####################################################

time.sleep(3)

    