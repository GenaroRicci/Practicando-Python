
#🛠 Explicación de la estructura:

# 1 Importaciones

#Librerías estándar

#Librerías de terceros

#Módulos locales (propios del proyecto)

#Ordenadas alfabéticamente y separadas por líneas en blanco

# 2 Definición de constantes

#Las constantes se escriben en mayúsculas con guiones bajos (CONFIG_PATH)

#Si hay configuraciones, se recomienda almacenarlas en archivos externos (JSON, .env, etc.)

# 3 Definición de funciones y clases

#Funciones: Dividir el código en funciones pequeñas y reutilizables

#Clases: Usar clases si el programa maneja estructuras de datos complejas

# 4 Función main()

#Es el punto central donde se ejecuta la lógica del programa

#Mantiene el código limpio y modular

# 5 Punto de entrada if __name__ == "__main__":

#Esto permite que el script pueda ejecutarse directamente o importarse como módulo sin ejecutarlo automáticamente.

import time
import math
import random

#Variables generales

errormsg = 'Error: Debes introducir un numero valido.'
nm0msg = 'Introduce un numero mayor a 0'

#Calculo de Salario

name = input('Introduzca tu nombre:\n')
print('Hola, ' + name)

horas = float(input('Cuantas horas trabaja usted?\n'))
try:
    if horas < 1:
        print(nm0msg)
        exit()
except ValueError:
    print(errormsg)
    exit()

try:
    tarifa = float(input('Cuanto cobra por hora?\n'))
    if tarifa < 0:
        print(nm0msg)
        exit()
    salario = float(horas) * float(tarifa) * 1.5
    round(salario)
    print(f'Su salario es {salario}')

except ValueError:
    print(errormsg)

#Datos para ver como funciona python y evaluar

ancho = 17
alto = 12.0

print(ancho / 2)
print(ancho / 2.0)
print(alto / 3)
print( 1 + 2 * 5)

#Celsius a Farenheit:

# Formula implementada: °F = (°C × 9/5) + 32

try:
    celsius = float(input('Coloque su temperatura en Celsius\n'))
    fahrenheit = celsius * 9/5 + 32
    print(f'Su temperatura son {fahrenheit:.2f} grados Farenheit')
except ValueError:
    print(errormsg)

#Radio de un circulo:

# Formula implementada: pi * radio al cuadrado

radius = float(input('Ingrese el radio de un circulo\n'))
try:
    area = math.pi * radius ** 2
    print(f'Su area es {area:.2f}')

except ValueError:
    print(errormsg)

#Ejecucion condicional

#Puntuacion entre 1.0 y 0.6

puntuacion = float(input('Indica tu puntuacion entre 0.0 y 1.0\n'))

try:
    if puntuacion >= 0.9: print('Sobresaliente')
    elif puntuacion >= 0.8: print('Notable')
    elif puntuacion >= 0.7: print('Bien')
    elif puntuacion >= 0.6: print('Suficiente')
    else: print('Insuficiente')

except ValueError:
    print(errormsg)

time.sleep(3)

#MODULO RANDOM:

#10 iteraciones de random entre 0.0 y 0.9 periodico:

for i in range (10):
    x = random.random()
    print(x)

# Numeros random entre 2 parametros:

random.randint(5,10)
random.randint(5,10)
random.randint(5,10)

#Numero random de una lista:

t = [1, 2, 3, 4, 5]

random.choice(t)
random.choice(t)

