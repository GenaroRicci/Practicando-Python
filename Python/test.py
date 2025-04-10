import time
import math
import random
errormsg = 'Error: Debes introducir un numero valido.'
nm0msg = 'Introduce un numero mayor a 0'

###################################################################


max = None
min = None

list = [3, 6, 13, 9, 55, 41, 34, 1, 765, 95]
try:
    for i in list:
        if max is None or i > max:
            max = i
        if min is None or i < min:
            min = i
    print(f'Su mayor numero es {max} y su menor es {min}')
except ValueError:
        print(errormsg)
##############################################

##############################################

















time.sleep(3)

