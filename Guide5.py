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
    
#5F
from random import randint
n = int(input("Ingrese la cantidad de jugadores: ")); val = int(input("Ingrese el valor a conseguir: ")); cont=False
for i in range(n):
    jVal=randint(1,6) ;print(f"El jugador {i+1} sacó {jVal}")
    if jVal==val: cont=True
if cont: print(f"Se ha conseguido el valor {val}")
else: print("No se ha conseguido el valor")

#5G
from random import randint
n = int(input("Ingrese la cantidad de dados: ")); high = 0
for i in range(n):
    jVal=randint(1,6); print(f"Dado {i+1}: {jVal}");
    if jVal>high: 
        high=jVal
print(f"Valor más alto: {high}")

#5H
from random import randint
puntaje = 0
for i in range(10):
    val=randint(1,20); 
    if val%2==0: par=True
    else: par=False
    user = input(f"El número (vez {i+1}) es par? (y/n) ")
    if user.upper()=="Y": uPar=True
    else: uPar=False
    if par and uPar: puntaje+=1
    print(f"El número era {val}")
print(f"Puntaje: {puntaje}")

#5I
alm = int(input("Ingrese la cantidad de alumnos: ")); pGen=0
for i in range(alm):
    pAlm=0
    for j in {1,2,3}:
        pAlm+=float(input(f"Ingrese la nota {j} del alumno {i+1}: "))
    print(f"El promedio del alumno {i+1} es de {round(pAlm/3,2)}")
    pGen+=pAlm/3
print(f"El promedio general del curso es de {round(pGen/3,2)}")

#5J
cant = int(input("Ingrese la cantidad de empleados: ")); slTotal=0; mTotal=0; fTotal=0;
for i in range(cant):
    slTotal+=float(input(f"Ingrese el sueldo del empleado {i+1}: ")); sxEmp=input(f"Ingrese el sexo del empleado {i+1}: (M/F)")
    if sxEmp.upper()=="M": mTotal+=1
    elif sxEmp.upper()=="F": fTotal+=1
    else:
        print("Qué, algún intrasexual?"); break
    
print(f"Empleados de sexo masculino: {mTotal}\nEmpleados de sexo femenino: {fTotal}\nSueldo promedio: {slTotal/cant}")

#5K
cant = int(input("Ingrese la cantidad de alumnos: ")); lv1=0; lv2=0; lv3=0;
for i in range(cant):
    agno = int(input(f"Ingrese el número del año del alumno {i+1} (ej:1 para Primer Año): "))
    if agno==1 or agno==2: lv1+=1
    elif agno==3 or agno==4: lv2+=1
    elif agno==5 or agno==6: lv3+=1
    else: print("Algo anda mal..."); break
    
print(f"Alumnos en el nivel 1: {lv1}\nAlumnos en el nivel 2: {lv2}\nAlumnos en el nivel 3: {lv3}")

#5L
count = 3
for i in range(count-1):
    count*=(i+1)
    print(count)
    

#5L v2
n = int(input("Ingrese hasta que número de términos quiere realizar la sucesión de Fibonacci: "))
count = 1; pre = 0
for i in range(n):
    print(count)
    count+=pre; pre=count-pre
    
#5M
n = int(input("Ingrese la cantidad de renglones: "))
for i in range(n+1): # a
    for j in range(i):
        print("*", end="")
    print()
for i in range(n+1): # b
    for j in range(i):
        print(j+1, end="")
    print()
for i in range(n,0,-1): # c
    for j in range(i):
        print("*", end="")
    print()
for i in range(n,0,-1): # d
    for j in range(i,0,-1):
        print(j, end="")
    print()
for i in range(n+1): # e y f A RESOLVER
    for j in range(i):
        p = "*"
        for k in range(j):p+="*"
        print(p, end="")
    print()

#5N A RESOLVER TAMBIEN
