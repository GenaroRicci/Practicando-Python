import time
import math
import random
errormsg = 'Error: Debes introducir un numero valido.'
nm0msg = 'Introduce un numero mayor a 0'

###################################################
dato = 'From stephen.merquard@utc.ac.za Sat Jan 5 09:14:16 2008'
positionarroba = dato.find('@') #Encuentra la posicion en el str
print(f'Posicion de arroba :{positionarroba}')
positionespacios = dato.find(' ', positionarroba)
print(f'Posicion del espacio :{positionespacios}')
adress = dato [positionarroba + 1: positionespacios] #Empieza desde la arroba, le suma 1 y llega hasta la posicion del espacio del dato
print(f'El adress es: {adress}')


##############################################

time.sleep(3)

