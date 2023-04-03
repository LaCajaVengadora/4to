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
