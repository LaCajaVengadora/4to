#6A
n = 0
for i in range(30):
    n += ((i+1)*3)
print(n/30)

n=0; k = 0
while k!=30:
    k+=1; n += (k*3)
print(n/30)

#6B
from random import randint
times = int(input("Ingrese la cantidad de tiradas: ")); right=0; wrong=0
for i in range(times):
    num = randint(1,6)
    choice = int(input(f"{i+1}.¿Qué n salió? "))
    if choice==num:
        right+=1; print(f"Correcto. Aciertos:{right}")
    else:
        wrong+=1; print(f"Incorrecto. Errores:{wrong}")
print(f"De {times} tiradas, {right} fue/ron correcta/s y {wrong} no lo fue/ron")

#6C
seguir = input("Ingrese si quiere iniciar el programa: (y) ").upper()
if seguir=="Y": seguir=True
else: seguir=False
while(seguir):
    char = input("Ingrese el carácter a repetir: "); num = int(input(f"Ingrese la cantidad de veces a repetir {char}: "))
    if num>50: 
        print(f"{num} es mayor que 50"); break
    for i in range(num):
        print(char, end='')
    print()
    seguir = input("Ingrese si quiere continuar con el programa: (y) ").upper()
    if seguir=="Y": seguir=True
    else: seguir=False
print("Fin")

#6D
n1 = int(input("Ingrese el primer número: "))
n2 = int(input(f"Ingrese el segundo número (menor que {n1})"))
while n2>=n1:
    print(f"{n2} NO es menor que {n1}", end=' ');n2 = int(input(f"Ingrese el segundo número devuelta (menor que {n1})"))
print(f"Los números son {n1} y {n2}")

#6E
Lista = []; divisores = 0
n = int(input("Ingrese un número. Se escribiran los números primos entre el 1 y tal número: "))
for i in range(n):
    for j in range(i+1): 
        if (i+1)%(j+1)==0: Lista.append(j+1)
    for k in Lista: divisores+=1
    if divisores==2 or divisores==1: print(i+1)
    Lista = []; divisores = 0
    
#6F EN TEORÍA...
def trueGetter(n):
    divisores = []; primos = []
    for i in range(n):
       if n%(i+1)==0: divisores.append(i+1)
    for i in divisores: #1
        divDivs = 0
        for j in range(i): 
            if (i)%(j+1)==0: 
                divDivs+=1
        if divDivs==2: primos.append(i)
    primos.reverse()
    return primos

num = int(input("Escriba un número mayor que 1: ")); tester = num
print("Descomposición en factores primos: "); print(trueGetter(num)); end=False
while not end:
    for i in trueGetter(num):
        if tester%i==0: 
            print(f"{tester}", end="")
            tester/=i
            if tester==1:break
            print(f" | {i}")
#6G
n = float(input("Ingrese un número: "))   
while True:
    current = float(input(f"Ingrese un número mayor que {n}: "))
    if current<=n:
        print(f"{current} no es mayor que {n}")
        break
        
#6H
n = int(input("Ingrese un número: "))
while True:
    current = int(input(f"Ingrese un número mayor que {n}: "))
    if current<=n:
        print(f"{current} no es mayor que {n}")
        break
    n=current
    
#6I
n = int(input("Ingrese un número positivo: "))
while n<=0: n = int(input("Ingrese un número POSITIVO: "))
pos = 0; neg = 0; cero = 0
for i in range(n):
    num = int(input(f"Ingrese un número (vez {i+1}): "))
    if num>0:pos+=1
    elif num<0:neg+=1
    else:cero+=1
print(f"Ha introducido {n} números, {pos} de ellos es/son positivo/s")

#6J
suma=0
while True:
    n = int(input("Escriba un número: "))
    if n>=0: suma+=n
    else: break
print(f"Suma de todos los números (menos el negativo): {suma}")

#6K
n = float(input("Ingrese un número positivo límite: ")); suma=0
while n<=0: n = float(input("Ingrese un número POSITIVO: "))
while suma<n:
    suma += float(input("Ingrese un número"))
print("Has superado el límite")

#6L
minum = int(input("Ingrese el mínimo: ")); maxum = int(input("Ingrese el máximo: ")); i=minum+1; counter=0
while i<=maxum and i>=minum:
    i = int(input(f"Ingrese un número entre {minum} y {maxum}: "))
    counter+=1
print(f"Escribiste {counter-1} números entre {minum} y {maxum}")

#6M
#6N
