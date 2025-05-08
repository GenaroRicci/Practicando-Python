import time
import math
import random
errormsg = 'Error: Debes introducir un numero valido.'
nm0msg = 'Introduce un numero mayor a 0'

###################################################
#

name_file = input('Ingresa el nombre de tu archivo:\n')
try:
    file_handler = open(name_file)
    counter = 0
    for line in file_handler:
        if line.startswith('Subject:'):
            counter = counter + 1
    print(f'Hay {counter} lineas en de asunto "Subject" en {name_file}')
except:
    print(f'No se pudo abrir el archivo: {name_file}')


#####################################################
time.sleep(3)

    