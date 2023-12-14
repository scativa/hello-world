print("Hello, World")

msg =("viva la vida")
print(msg)

help("keywords")

TOTAL_POPULATION =44000000
print (TOTAL_POPULATION)

type (TOTAL_POPULATION)


space_odyssey =2001
print(space_odyssey)

type ("Good night & Good luck")


type ("true")
print (type)

result =10*(3,0)
print (result)


Original= [1,2,3]
copy=Original
print (copy)

#Modify first element
Original [0]=99
print(copy)

#Assign new object
Original= [4,5,6]
print(Original)

a=3.14
print(type(a))
c=10
d=4
e=c/d
print (e)

j=4e3
print (j)

c=2+6j
e=2+2j
print (c+e)

d= True *9
print (d)

#Cat Age
e=int(input("Ingrese la edad de su gato: "))
b=e+15
c=b+9
d=c+4

print (d)

#Dog Age
a=int(input("Ingrese la edad de su perro: "))
b=[a,a+15]
c=[b,b[1]+9]
d=[c,c[1]+5]

print (d)
print(b)

#Aspect Radio Cropping

import math

def convertir_aspecto_16_9(X, Y):
    # Definir la relación de aspecto 16:9
    aspect_ratio = 16 / 9
    
    # Calcular la nueva resolución X
    new_X = math.ceil(Y * aspect_ratio)
    
    # Devolver la nueva resolución
    return new_X, Y

# Ejemplo de uso
X_original = 1440
Y_original = 1080

nueva_resolucion = convertir_aspecto_16_9(X_original, Y_original)
print(f"Resolución original: {X_original}x{Y_original}")
print(f"Resolución ajustada: {nueva_resolucion[0]}x{nueva_resolucion[1]}")

#Convercion USD a Yuan

# Supongamos que tienes un dato previo en la variable dato_previo
dato_previo = 33.8

# Calcula el resultado multiplicando por 6.75
resultado = 6.75 * dato_previo

# Expresa el resultado con dos decimales y la frase "Chinese Yuan"
resultado_formateado = "{:.2f} Chinese Yuan".format(resultado)

# Imprime el resultado formateado
print(resultado_formateado)


#Redondeo de númers

import math

numero= 8.75

numero_redondeado=math.ceil(numero)

print(numero_redondeado)

msg=("intento de salto de primera linea \n a segunda linea")
print (msg)

msg=("valor de x=65")
print (msg)

#calculo del tercer angulo de un triangulo

def third_angle(angle1, angle2):
    # Calculate the third angle
    angle3 = 180 - angle1 - angle2
    
    return angle3

# Example usage:
angle1 = 70
angle2 = 35

result = third_angle(angle1, angle2)
print(f"The third angle is: {result} degrees")

name= "Elion Musk"
age= 49
fortune= 4000

msg= f"Me llamo {name}, tengo {age} años de edad, y una fortuna de {fortune} millones"
print(msg)

a=10
print(a)

#Ejercicios STRINGS
c = 2.71828
print(f"{c:.3f}")

print(f"{c:.6f}")

print(f"{c:8.2f}")

print(f"{c:e}")

print(f"{c:010.4f}")

print(f"{c:19.5f}")


#If

value = 23

if value is not None:
    print(f"value={value}")

#Sentencia Match_case

def calcular_resultado(num1, num2, operando):
    resultado = None

    match operando:
        case '+':
            resultado = num1 + num2
        case '-':
            resultado = num1 - num2
        case '*':
            resultado = num1 * num2
        case '/':
            resultado = num1 / num2
        case _:
            print("Operación no válida. Por favor, elija una de las siguientes: '+', '-', '*', '/'")

    return resultado

# Solicitar valores al usuario
num1 = float(input("Ingrese el primer valor numérico: "))
num2 = float(input("Ingrese el segundo valor numérico: "))
operando = input("Ingrese el operando (+, -, *, /): ")

# Calcular el resultado
resultado = calcular_resultado(num1, num2, operando)

# Mostrar el resultado si la operación es válida
if resultado is not None:
    print(f"{num1} {operando} {num2} = {resultado}")

#Ejercicios Pág 127

def get_weekday(number):
    if 1 <= number <= 7:
        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return weekdays[number - 1]
    else:
        return "Wrong, please enter a number between 1 and 7"

# Example usage:
number_input = int(input("Enter a number between 1 and 7: "))
result = get_weekday(number_input)
print(result)


def make_negative(number):
    return -abs(number)

# Example usage:
input_number = float(input("Enter a number: "))
result = make_negative(input_number)
print(f"The negative version of {input_number} is {result}")

#American Floor
def american_to_european_floor(american_floor):
    if american_floor == 0:
        return -1
    elif american_floor >= 13:
        return american_floor - 2  # Move down by two for floors above 13
    else:
        return american_floor - 1
    
# Example usage:
american_floor = int(input("Enter the American floor number: "))
european_floor = american_to_european_floor(american_floor)
print(f"The European floor number is: {european_floor}")

#Bucles

# Importante dar un valor antes de empezar el bucle
want_exit = "N"
num_question = 0  # Inicializamos la variable num_question

while want_exit == "N" and num_question < 4:
    print("Hola, ¿qué tal?")
    want_exit = input("¿Quiere salir? [S/N]")
    num_question += 1
print("¡Ciao!")

#Break
want_exit = "N"	
num_questions = 0
while want_exit == "N":
    print("Hola qué tal")
    want_exit = input("¿Quiere salir? [S/N]")
    num_questions += 1
    if num_questions == 4:
        print("Máximo número de preguntas alcanzado")
        break
    else:
        print("Usted ha decidido salir")
        print("Ciao")

        #continuar un bucle

want_exit = "N"	
valid_options = 0
while want_exit == 	"N":
    print("Hola qué tal")
    want_exit = input("¿Quiere salir? [S/N]")
    if want_exit not in 	"SN"	:
        want_exit = "N"	
        continue
    valid_options += 1
    print(f"{valid_options}respuestas válidas")
    print("Ciao!")

#Bucle infinito(Nota fuera de rango)

while True:
    mark = float(input("Introduzca nueva nota: "))
    if not(0 <= mark <= 10):
        print("Nota fuera de rango")
        break
    print(mark)

    #Operador Morsa

while True:
    mark = float(input("Introduzca una nueva nota: "))
    
    if 0 <= mark <= 10:
        print(f"La nota ingresada es: {mark}")
    else:
        print("Nota fuera de rango")
        break

#Ejercicio pág 134
#Escribir los multiples de 5 menores al valor ingresado

def multiples_of_5(limit):
    multiples = [num for num in range(5, limit) if num % 5 == 0]
    return multiples

# Solicitar al usuario ingresar el límite
limit = int(input("Ingrese un valor límite: "))

# Obtener los múltiplos de 5 menores que el límite
result = multiples_of_5(limit)

# Mostrar los resultados
print(f"Los múltiplos de 5 menores que {limit} son: {result}")

#Sentencia For(datos Iterables)

Word="Nomencaltura"
for Letter in Word:
    print("Nomenclatura")

#Romper un bucle For

Word="Friday"

for Letter in Word:
  if Letter =="i":
    break
  print(Letter)

#Ejercicio cantidad de vocales

Word="Supercalifragilisticoespialidoso"

#definir una lista de vocales

vocales= "aeiou"

#iniciar el contador de vocales
contador_vocales=0

for letter in Word:
 #verificar si la letra es una vocal
 if letter in vocales:
    contador_vocales +=1

    print(contador_vocales)

# Imprimir el total de vocales
print(f"El total de vocales en '{Word}' es: {contador_vocales}")

#Ejercicios Bucles Anidados

for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(f"{i} * {j} = {result}")