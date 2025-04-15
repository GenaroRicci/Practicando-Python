import time
import math
import random
errormsg = 'Error: Debes introducir un numero valido.'
nm0msg = 'Introduce un numero mayor a 0'

###################################################

def cuenta(palabra, letra):
    counter = 0
    for character in palabra:
        if character == letra:
            counter = counter + 1
    print(counter)

cuenta('sdiffdgisfjsdfsdfkdsofsgod', 'f')

##############################################

time.sleep(3)

