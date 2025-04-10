# 🛠 Explicación de la estructura:

# 1 Importaciones

# Librerías estándar

# Librerías de terceros

# Módulos locales (propios del proyecto)

# Ordenadas alfabéticamente y separadas por líneas en blanco

# 2 Definición de constantes

# Las constantes se escriben en mayúsculas con guiones bajos (CONFIG_PATH)

# Si hay configuraciones, se recomienda almacenarlas en archivos externos (JSON, .env, etc.)

# 3 Definición de funciones y clases

# Funciones: Dividir el código en funciones pequeñas y reutilizables

# Clases: Usar clases si el programa maneja estructuras de datos complejas

# 4 Función main()

# Es el punto central donde se ejecuta la lógica del programa

# Mantiene el código limpio y modular

# 5 Punto de entrada if __name__ == "__main__":

# Esto permite que el script pueda ejecutarse directamente o importarse como módulo sin ejecutarlo automáticamente.

import time
import math
import random

# Variables generales

errormsg = "Error: Debes introducir un numero valido."
nm0msg = "Introduce un numero mayor a 0"

# Calculo de Salario

name = input("Introduzca tu nombre:\n")
print("Hola, " + name)


def calculosalario():

    try:
        horas = float(input("Cuantas horas trabaja usted?\n"))
        if horas < 1:
            print(nm0msg)
            return
    except ValueError:
        print(errormsg)
        return

    try:
        tarifa = float(input("Cuanto cobra por hora?\n"))
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

    print(f"Su salario es {salario:.2f}")


# Datos para ver como funciona python y evaluar

ancho = 17
alto = 12.0

print(ancho / 2)
print(ancho / 2.0)
print(alto / 3)
print(1 + 2 * 5)

# Celsius a Farenheit:

# Formula implementada: °F = (°C × 9/5) + 32

try:
    celsius = float(input("Coloque su temperatura en Celsius\n"))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"Su temperatura son {fahrenheit:.2f} grados Farenheit")
except ValueError:
    print(errormsg)

# Radio de un circulo:

# Formula implementada: pi * radio al cuadrado

radius = float(input("Ingrese el radio de un circulo\n"))
try:
    area = math.pi * radius**2
    print(f"Su area es {area:.2f}")

except ValueError:
    print(errormsg)

# Ejecucion condicional

# Puntuacion entre 1.0 y 0.6


def puntuacion(a):
    try:
        if a >= 0.9:
            print("Sobresaliente")
        elif a >= 0.8:
            print("Notable")
        elif a >= 0.7:
            print("Bien")
        elif a >= 0.6:
            print("Suficiente")
        else:
            print("Insuficiente")

    except ValueError:
        print(errormsg)


time.sleep(3)

# MODULO RANDOM:

# 10 iteraciones de random entre 0.0 y 0.9 periodico:

for i in range(10):
    x = random.random()
    print(x)

# Numeros random entre 2 parametros:

random.randint(5, 10)
random.randint(5, 10)
random.randint(5, 10)

# Numero random de una lista:

t = [1, 2, 3, 4, 5]

random.choice(t)
random.choice(t)

# Definir funciones


def muestra_estribillo():
    print("Soy un leñador, que alegria!")
    print("Duermo toda la noche y trabajo todo el dia")


# Anidar funciones


def repite_estribillo():
    muestra_estribillo()
    muestra_estribillo()


# Ejecucion de funciones

repite_estribillo()

# ITERACION:

# Funcion de despegue juju:

print("Atentos maidai maidai, cuidado con las siguientes indicaciones: ATENCION!!")

time.sleep(2)

print("El cohete despegara en: \n")

time.sleep(1)

n = 5

while n > 0:
    print(n)
    n = n - 1
    time.sleep(1)

print("Despegue!!")

# Repetidor de palabras:

print(
    'Esto es un repetidor! Escriba lo que desees, el programa solo se cerrara cuando typees exactamente "exit"'
)

while True:
    a = input("> ")
    print(a)
    if a == "exit":
        break
print("Espero hayas disfrutado el programa!")

################################################

# TRABAJOS DE ITERACION CON LISTAS:

# Recorriendo lista:
amigos = ["Joseph", "Glenn", "Sally"]
for amigo in amigos:
    print(f"Buenos dias querido :{amigo}")
print("Cvmooo")

time.sleep(3)

##################################################

# Contador de cantidad

counter = 0

list_el1 = [1, 2, 3, 8, 5, 6, 7, 8]

for elemento in list_el1:
    counter = counter + 1
print(f"Su lista tiene {counter} elementos")

########################################################

# Suma de elementos

total = 0
list_el2 = [5, 324, 6, 123, 5, 4, 6]
for i in list_el2:
    total = total + i
print(f"Su total es: {total}")

########################################################

# Encontrar mayor:

try:
    while True:
        mayor = None
        print(f"Antes: {mayor}")
        for i in [3, 41, 12, 9, 74, 15]:
            if mayor is None or i > mayor:
                mayor = i
            print(f"Bucle: {i} {mayor}")
        print(f"El mayor numero es: {mayor}")
except:
    print("Se ignoro un valor invalido")

##########################################################

# Encontrar menor:

try:
    menor = None
    print(f"Antes: {menor}")
    for i in [3, 41, 12, 9, 74, 15]:
        if menor is None or i < menor:
            menor = i
        print(f"Bucle: {i} {menor}")
    print(f"El menor numero es: {menor}")
except:
    print("Se ignoro un valor invalido")

################################################################

# Una vez se haya introducido “fin”,
# muestra por pantalla el total, la cantidad de números y la media de
# esos números.

total = 0
counter = 0
errormsg = " Error: Ingrese un número válido."

while True:
    value = input("Introduzca un número:\n")

    if value == "fin":
        if counter > 0:
            media = total / counter
            print(
                f"El total es: {total:.2f}, la cantidad es: {counter} y el promedio es: {media:.2f}"
            )
        else:
            print("No se ingresaron números válidos.")
        break

    try:
        total = total + float(value)
        counter = counter + 1
    except ValueError:
        print(errormsg)

###########################################################################

# EJERCICIO DE CHATGPT🧩 Ejercicio: Números positivos y negativos

# Escribí un programa que lea repetidamente números desde el teclado.

# Cuando el usuario escriba "fin", el programa debe mostrar:

# la suma total de los números positivos,

# la suma total de los números negativos,

# y cuántos números válidos se ingresaron en total.

# 🧠 Si el usuario escribe algo que no sea un número (ni "fin"), mostrale un mensaje de error con try/except.

positivos = 0
negativos = 0
total = 0

while True:
    print('Ingresa un numero, Ingresa "fin" para acabar')
    valor = input("> ")

    if valor == "fin":
        print(f"La suma total de los numeros positivos es: {positivos}")
        print(f"La suma total de los negativos es: {negativos}")
        print(f"La suma total de los numeros es: {total}")
        break
    try:

        valor = float(valor)
        total += valor
        if valor == 0:
            continue
        if valor > 0:
            positivos += valor
        if valor < 0:
            negativos += valor

    except ValueError:
        print(errormsg)
