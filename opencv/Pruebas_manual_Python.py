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

result =10*3,0
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
a=1
b=a+15
c=b+9
d=c+4

print (d)

#Dog Age
a=1
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
