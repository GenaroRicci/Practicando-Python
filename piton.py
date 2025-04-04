
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

def calculosalario():

    try:
        horas = float(input('Cuantas horas trabaja usted?\n'))
        if horas < 1:
            print(nm0msg)
            return
    except ValueError:
        print(errormsg)
        return

    try:
        tarifa = float(input('Cuanto cobra por hora?\n'))
        if tarifa <= 0:
            print(nm0msg)
            return
    except ValueError:
        print(errormsg)
        return

    if horas > 40:
        horasextra = horas - 40 
        salario = (40 * tarifa) + (horasextra * tarifa * 1.5)
    else:
        salario = float(horas) * float(tarifa)
    
    print(f'Su salario es {salario:.2f}')

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

def puntuacion(a):
    try:
        if a >= 0.9: print('Sobresaliente')
        elif a >= 0.8: print('Notable')
        elif a >= 0.7: print('Bien')
        elif a >= 0.6: print('Suficiente')
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

#Definir funciones

def muestra_estribillo():
    print('Soy un leñador, que alegria!')
    print('Duermo toda la noche y trabajo todo el dia')

#Anidar funciones

def repite_estribillo():
    muestra_estribillo()
    muestra_estribillo()

#Ejecucion de funcionesw

repite_estribillo()

#ITERACION:

#Funcion de despegue juju:

n = 5
while n > 0:
    print(n)
    n = n-1
print('Despegue!!')
