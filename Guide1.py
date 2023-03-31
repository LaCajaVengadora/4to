from math import pow, sqrt

#1A print("Hello world")
'''Link no disponible de página ASCII'''
#1C n = input("Introduce tu nombre: "); print("Hola",n)

#1D
day = int(input("Introduce el día de tu nacimiento: "))
mes = int(input("Introduce el mes de tu nacimiento: "))
print(f"La suma de esos números es {day+mes}")

#1E
print(((3+22*5)**2)/((3/2)+47.8))

#1F
b = int(input("Introduce la base de un triángulo: "))
h = int(input("Introduce la altura de un triángulo: "))
hip = sqrt(pow(b,2)+pow(h,2))
print(f"El perímetro del triángulo es {h+b+hip}cm\nY su área es {(h*b)/2}cm²")
