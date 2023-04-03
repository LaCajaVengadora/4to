#3A
n =  int(input("Ingrese un número entero: "))
if n%2==0: print(f"{n} es par")
else: print(f"{n} es impar")
  
#3B ya hecho en 2B

#3C
n1 =  float(input("Ingrese el lado 1 de un triángulo: "))
n1 +=  float(input("Ingrese el lado 2 de un triángulo: "))
n1 +=  float(input("Ingrese el lado 3 de un triángulo: "))
if n1==180: print("Los lados suman 180, por ende, podrían ser los lados de un triángulo")
else: print("Los lados NO suman 180, por ende, NO podrían ser los lados de un triángulo")
  
#3D
edad = int(input("Ingrese su edad: "))
if edad>70 or edad<18: print("No puede tramitar")
else: print("Si puede tramitar")
  
#3E
n = float(input("Ingrese un número del 1 al 10"))
while n>10 or n<1: 
    n = float(input("Ingrese un número DEL 1 AL 10"))
for i in range(10):
    print(n*(i+1))

#3F
precio = float(input("Ingrese el precio del producto")); pay = input("Ingrese el método de pago (efectivo|credito|debito)")
if pay=="credito": print("Tenés que pagar",precio*1.21)
elif pay == "debito": print("Tenés que pagar",precio)
elif pay == "efectivo": print("Tenés que pagar",precio*0.9)
else: print("O escribiste mal, o escribiste cualquier cosa")
  
#3G
n1 = int(input("Ingrese el dividendo ENTERO de una división")); n2 = int(input("Ingrese el divisor ENTERO de una división"))
try:
    print(f"{n1} dividido {n2} es {n1/n2}", end=" y ")
    if n1%n2==0: print("es una división entera")
    else: print("no es una división entera")
except ZeroDivisionError: print("No se puede dividir por 0")

#3H
from math import pi
shape = input("Ingrese si quiere calcular el área de un círculo o un triángulo (C / T): ")
if shape.upper()=="T":
    b = float(input("Ingrese la base del triángulo (cm): ")); h = float(input("Ingrese la altura del triángulo (cm): "))
    print(f"El área de ese triángulo es de {b*h/2}cm²")
elif shape.upper()=="C":
    r = float(input("Ingrese el radio del círculo (cm): "))
    print(f"El área de ese círculo es de {round(r*r*pi,2)}cm²")
else:
    print("Poné C o T")

#3I
n1 = float(input("Ingrese el primer número: ")); n2 = float(input("Ingrese el segundo número: "))
if n1>n2: print(f"{n1} es mayor que {n2}")
elif n1<n2: print(f"{n2} es mayor que {n1}")
else: print(f"{n1} y {n2} son iguales")
  
#3J
agnoNow = int(input("Ingrese el año actual: ")); agnoThen = int(input("Ingrese un año cualquiera: "))
if agnoNow>agnoThen:
    print(f"Estando en {agnoNow}",end=" ")
    if agnoNow-agnoThen==1: print(f"ha pasado 1 año desde {agnoThen}")
    else: print(f"han pasado {agnoNow-agnoThen} años desde {agnoThen}")
elif agnoThen>agnoNow:
    print(f"Estando en {agnoNow}",end=" ")
    if agnoThen-agnoNow==1: print(f"falta 1 año para {agnoThen}")
    else: print(f"faltan {agnoThen-agnoNow} años para {agnoThen}")
else:
    print(f"{agnoNow} es el mismo año que {agnoThen}")
    
#3K
n1 = int(input("Ingrese el primer número: ")); n2 = int(input("Ingrese el segundo número: "))
if n1<=0 or n2<=0:
    print("No se aceptan números negativos o 0")
else:
    if n1>n2: 
        mayor=n1;menor=n2
    elif n1<n2:
        mayor=n2;menor=n1
    else:
        mayor=n1; menor=n1
        print("Son el mismo número. Aún asi,",end=" ")
    if mayor%menor==0: print(f"{mayor} es múltiplo de {menor}")
    else: print(f"{mayor} NO es múltiplo de {menor}")

#3L
n1 = float(input("Ingrese el primer número: ")); n2 = float(input("Ingrese el segundo número: ")); n3 = float(input("Ingrese el tercer número: "))
if n1==n2 and n2==n3: print("Los tres números son iguales")
elif n1==n2 or n2==n3 or n1==n3: print("Hay dos números iguales")
else: print("Los tres números son distintos")
 
#3M
n = int(input("Ingrese un número: "))
if n>0 and n%2==0: print(f"{n} es positivo y par")
elif n<0 and n%2==0: print(f"{n} es negativo y par")
elif n>0 and n%2!=0: print(f"{n} es positivo e impar")
elif n<0 and n%2!=0: print(f"{n} es negativo e impar")
else: print("0 es neutro y par")

#3N TODO-------------------------------------------------
a = float(input("Ingrese A (coeficiente principal): "))
b = float(input("Ingrese B (coeficiente lineal): "))
c = float(input("Ingrese C (término indepentiente): "))
