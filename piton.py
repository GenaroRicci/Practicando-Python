import time
import math
import random

name = input('Introduzca tu nombre:\n')
print('Hola, ' + name)

horas = float(input('Introduce horas:\n'))
tarifa = float(input('Introduce tarifa por hora:\n'))
salario = round((horas) * (tarifa))

try:
    if horas > 40 :
        salario = round(40 * tarifa) + (horas - 40) * (tarifa * 1.5)

except ValueError:
    print('Introduzca numeros para horas y/o salario.\n')


print('Su salario es: ' + str(salario)) 

try:
    note = float(input('Introduzca puntuacion\n'))
    if note > 1.0:
        raise ValueError('Puntuacion incorrecta.')
    elif note < 0.6:
        print('Insuficiente')
    elif note < 0.7:
        print('Suficiente')
    elif note < 0.8:
        print('Bien')
    elif note < 0.9:
        print('Notable')
    elif note < 1.0:
        print('Insuficiente')

except ValueError:
    print('Error: Introduzca un número válido entre 0.0 y 1.0 para la puntuación.')

print(math)

print(random.randint(5,10), 
random.randint(5,10), 
random.choice([1,2,3,4,5,6,7,8,9]),
random.choice([1,2,3,4,5,6,7,8,9])
)

#* Functions.

def muestra_estribillo():
    print('Soy un leñador, que alegria!')
    print('Duermo toda la noche y trabajo todo el dia.')



time.sleep(5)





















time.sleep(3)





























