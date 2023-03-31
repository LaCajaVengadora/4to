from math import sqrt

#2.A)
#name = input("Ingrese su nombre: "); ap = input("Ingrese su apellido: ")
#print(f"Tu nombre es {name} y tu apellido es +{ap}")

#2.B)
#n1 = (float(input("Ingrese el num 1: "))); n2 = (float(input("Ingrese el num 2: ")))
#print(f"La suma de esos números es {n1+n2};\nLa resta es {n1-n2};\nLa multiplicación es {n1*n2}")
#try: print(f"La división es {round(n1/n2,2)}")
#except ZeroDivisionError: print("No se puede dividir por 0")

#2.C
#b = int(input("Introduce la base de un rectángulo: ")); h = int(input("Introduce la altura: ")); hip = sqrt(pow(b,2)+pow(h,2))
#print(f"El perímetro del triángulo es {round(2*h+2*b,2)}cm\nY su área es {round(h*b,2)}cm²\nPor último, su diagonal es {round(hip,2)}")

#2.D
'''pol = int(input("Introduzca la cantidad de lados del poligono REGULAR: "))
long = float(input("Introduzca la medida de uno de esos lados: "))
print(f"El perímetro es {pol*long}")'''

#2.E
'''valor_dolar = float(input("Cuanto vale el dolar en relación al peso (Ej: 1 peso = 0.0025 dolares): "))
valor_euro = float(input("Cuanto vale el dolar en relación al peso (Ej: 1 peso = 0.0047 euros): "))
peso=float(input("Introduzca la cantidad de pesos a cambiar: "))
print(f"{peso} pesos son: {round(peso*valor_dolar,2)} dolares y {round(peso*valor_euro,2)} euros")'''

#2.F
#n1 = int(input("Introduce el divisor")); n2 = int(input("Introduce el dividendo"))
#print(f"En división entera, {n1} dividido {n2} es {n1//n2} y el resto es {n1%n2}")

#2.G
#pies = float(input("Introduce la cantidad de pies a pasar a cm: "))
#print(f"{pies} pies son {pies*2.54*12}cm")

#2.H
#p = float(input("Introduce tu peso en kg: ")); h = float(input("Introduce tu altura en metros: "))
#print(f"Tu IMC es {round(p/(h**2),2)}")

#2.I + 2.J
'''trueSeg = int(input("Introduce la cantidad de segundos a convertir: "))
min = trueSeg//60; seg = trueSeg%60
hrs = min//60; min%=60
print(f"{trueSeg} segunds son {hrs} horas; {min} minutos y {seg} segundos")'''

DNI = input("Introduce tu DNI: "); g = input("Introduce si naciste siendo hombre o mujer (h/m): ")
if g=='h': first='20'
elif g=='m': first='27'
else: print("Todo bien, pero no podemos calcularlo"); error=True
if error:
    pass
else:
    CUIL=first+DNI
    InvCUIL=CUIL[::-1]; ver=0; count=0
    for i in [2,3,4,5,6,7,2,3,4,5]:
        nCUIL=int(InvCUIL[count]); count+=1
        ver+=(i*nCUIL)
    ver%=11; ver=11-ver
    CUIL+=str(ver)
    print(CUIL)
