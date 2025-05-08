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

###################################################

#Ejercicio 2 listas: Escribe otro programa que pida una lista de números como
#la anterior y al final muestre por pantalla el máximo y mínimo de los
#números, en vez de la media.

listain = input('>')
lista1 = []

for n in listain.split(','):
    try:
        numero = float(n.strip())
        lista1.append(numero)
    except ValueError:
        print(f'{errormsg} Valor ignorado: "{n.strip()}"')

if lista1:
    maximo = max(lista1)
    minimo = min(lista1)
    print(f'Su mayor numero es {max} y su menor numero es {min}')
else:
    print('No hay numeros validos')

#############################################################
#Listas

#Ejercicio 1: Escribe un bucle while que comience con el último carácter
#en la cadena y haga un recorrido hacia atrás hasta el primer carácter
#en la cadena, imprimiendo cada letra en una línea independiente.

fruta = 'banana'
i = len(fruta)
while i > 0:
    print(fruta[i-1])
    i = i-1

###################################################
#Recorrer
for character in fruta:
    print(character)

###################################################
#Rebanar str

print(fruta[0:])
print(fruta[0:3])
print(fruta[3:])

###################################################
#Concatenar str

saludo = 'Hello world'
nuevo_saludo = saludo[0:] + ', you are god!'

###################################################
#Contador

palabra = 'banana'
counter = 0
for letra in palabra:
        if letra == 'a' :
            counter = counter + 1
print(counter)

#Este programa demuestra otro patrón de computación llamado contador. La variable contador es inicializada a 0 y después se incrementa cada vez que una “a” es encontrada. Cuando el bucle termina, contador contiene el resultado: el número total de a’s.

###################################################
#Definiendo funcion de contador;

def contador(palabra, letra):
    counter = 0
    for character in palabra:
        if character == letra:
            counter =+ 1
    return counter

###################################################
#Operador in

"'a' in 'banana'"
'True'
#Capta letras
"'semilla' in 'banana'"
'False'
#No logica

###################################################
#Operaciones de comparacion en strings:

if palabra < 'banana':
    print(f'Tu palabra {palabra} esta antes de banana')
elif palabra > 'banana':
    print(f'Tu palabra {palabra} esta despues de banana')
else:
    print('muy bien, bananas')

#MAYUSCULAS PRIMERO A MINUSCULAS
#Piña antes que banana
#Para ordenar alfabeticamente por ejemplo, conviene convertir a un formato estandar:
#Ej todas minusculas: palabra.lower()

#####################################################
#Programa de contraseña para usuario chatgpt:

correct_pswd = 'Paiton'
user_pswd = ''
while user_pswd != correct_pswd:
    user_pswd = input('Escribe tu contraseña:\n')
    print('Incorrecta')
print('Contraseña aceptada!')

#####################################################
#Extrayendo datos particulares de un string

dato = 'From stephen.merquard@utc.ac.za Sat Jan 5 09:14:16 2008'
positionarroba = dato.find('@') #Encuentra la posicion en el str
print(f'Posicion de arroba :{positionarroba}')
positionespacios = dato.find(' ', positionarroba)
print(f'Posicion del espacio :{positionespacios}')
adress = dato [positionarroba + 1: positionespacios] #Empieza desde la arroba, le suma 1 y llega hasta la posicion del espacio del dato
print(f'El adress es: {adress}')

######################################################
#Te paso mail, conseguime nombre y apellido y edad:
mail = 'Genaro_Ricci_26@gmail.com'
endname = mail.find('_')#Encuentra donde limita nombre y da un int
endsurname = mail.find('_', endname +1)
endage = mail.find('@', endsurname+1)
name = mail[0: endname]
surname = mail[endname+1: endsurname]
age = mail[endsurname+1: endage]
print(name)
print(surname)
print(age)
#######################################################
#Codigo mas pro:

mail = 'Genaro_Ricci_26@gmail.com'

partes = mail.split('_') #['Genaro', 'Ricci', '26@gmail.com']
name = partes[0] 
surname = partes[1]
age = int(partes[2].split('@')[0])#Python va a resolver el parentesis y recien ahi aplicara la funcion int, el parentesis se resuelve de izquierda a derecha
print(name, surname, age)

#######################################################
#Utiliza find y una parte de la cadena para extraer la porción de la cadena, después del carácter dos puntos y después utiliza la función float para convertir la cadena extraída en un número de punto flotante.

stringfind = 'X-DSPAM-Confidence:0.8475'
numb = stringfind.find(':')
nuevo_num = float(stringfind[numb+1:])
print(nuevo_num)

#######################################################
#Probando count
#str.count(substring, start osea posicion del string donde empieza, end posicion del string donde termina)
string_1 = 'bdbfndfdfjdujasodkasodrhgwweifbbbb'
counted = string_1.count('b')
print(counted)

#########################################################

#Probando replace:
text_1 = 'apple apple apple'
print(text_1.replace('apple', 'orange', 2))
#output -> orange orange apple

##########################################################
#Contando lineas de archivo

manejador_archivo = open('mbox.txt')
counter = 0
for linea in manejador_archivo:
    counter = counter + 1
print(f'Contador de lineas : {contador}')

##########################################################
#Lee el archivo
manejador_archivo = open('mbox.txt')
inp = manejador_archivo.read()
print(len(inp))
print(inp[:20])

###########################################################
#Startswith para busqueda smart
try:
    manejador_archivo = open('mbox.txt')
    counter_lineas = 0
    for linea in manejador_archivo:
        linea = linea.rstrip()#Elimina todos los espacios en blanco A LA DERECHA (R de right strip)de una cadenas
        if linea.startswith('From:'):
            counter_lineas = counter_lineas + 1
            print(linea)
    print(f'El total de lineas de redactores es: {counter_lineas}')
except FileNotFoundError:
    print('No se pudo acceder al archivo')
#########################################################
#Metodo find para encontrar algo en particular:

man_a = open('mbox.txt')
for linea in man_a:
    linea = linea.strip()
    if linea.find('@uct.ac.za') == -1: continue
    print(linea)
####################################
#Metodo alterno mas simple:
man_a = open('mbox.txt')
for linea in man_a:
    linea = linea.strip()
    if '@uct.ac.za' not in linea:
        continue
    print(linea)
#########################################################
#Hacer que el archivo lo maneje el usuario:
name_file = input('Ingresa el nombre del archivo para escanear\n')
file_handler = open(name_file)
counter = 0
for linea in file_handler:
    if linea.startswith('Subject:'):
        counter += 1
print(f'Hay {counter} lineas de asunto "Subject" en {name_file}')

############################################################
#Evitamos los trolles:

name_file = input('Ingresa el nombre de tu archivo:\n')
try:
    file_handler = open(name_file)
except FileNotFoundError:
    print(f'No se pudo abrir el archivo: {name_file}')
    exit()
#Buena practica no usar el try except en todo el codigo, sino en lo que puede fallar unicamente


counter = 0
for line in file_handler:
    if line.startswith('Subject:'):
        counter += 1

print(f'Hay {counter} lineas en de asunto "Subject" en {name_file}')

#################################################################

#pag 90












