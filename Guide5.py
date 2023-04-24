#5A
for i in range(5): #O bueno, n cantidad de veces
    print("hola")
    
#5B
val = int(input("Ingrese un num hasta el cual será la escala: ")); jump = int(input("Ingrese el salto: "))
for i in range(0,val+1,jump):
    print(i)
    
#5C
n = float(input("Ingrese un num del 1 al 10: "));
while n<=0 or n>10:
    n = float(input("Ingrese un num del 1 al 10: "));
for i in range(10):
    print((i+1)*n)
    
#5D
from random import shuffle
n = int(input("Ingrese la cantidad de datos: "));
datos = []
for i in range(n):
    bit = input(f"Ingrese el dato {i+1}"); datos.append(bit)
shuffle(datos)
for i in datos:
    print(i, end=" ")
    
#5E
from random import randint
n = int(input("Ingrese la cantidad de jugadores: "));
for i in range(n):
    print(f"El jugador {i+1} sacó {randint(1,6)}")
    
#5F -------------------------to-do------------
from random import randint
n = int(input("Ingrese la cantidad de jugadores: "));
val = int(input("Ingrese el valor a conseguir: ")); cont=False
for i in range(n):
    jVal=randint(1,6) ;print(f"El jugador {i+1} sacó {jVal}")
    if jVal==val: con=True
if cont: print("Se ha conseguido el valor")
#5G
#5H
#5I
