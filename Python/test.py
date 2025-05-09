import time
import math
import random
errormsg = 'Error: Debes introducir un numero valido.'
nm0msg = 'Introduce un numero mayor a 0'

###################################################

file_name = input("Escribe el nombre de tu archivo\n")

if file_name =="na na boo boo":
    print("NA NA BOO BOO PARA TI - Te he atrapado!")
    quit()

try:
    file_handler = open(file_name)
except FileNotFoundError:
    print(f'Tu archivo "{file_name}" no fue encontrado.')
    quit()

counter = 0
total_number = 0
for line in file_handler:
    if line.startswith("X-DSPAM-Confidence:"):
        total_number += float(line.split(":")[1].strip())
        counter += 1
if counter:
    print(f"El total de los valores en promedio es {total_number/counter:.4f}")
else:
    print("No se encontraron lineas que coincidan")
#####################################################
time.sleep(3)

    