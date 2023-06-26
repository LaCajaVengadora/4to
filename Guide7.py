#7A
pedirNumero = lambda:float(input("Ingrese un número: "))
suma = lambda a,b:a+b; resta = lambda a,b:a-b; multi = lambda a,b:a*b
def div(a,b):
    try: return round(a/b,2)
    except ZeroDivisionError:
        print("División por 0 indeterminada")
        return null
def Mensaje(*args):print(args)

A=pedirNumero(); B=pedirNumero()
S=suma(A,B); R=resta(A,B); M=multi(A,B); D = div(A,B)
Mensaje(S,R,M,D)

#7B
FtoC= lambda f:round((f-32)*5/9,2)
CtoF= lambda c:round(c*9/5+32,2)
print(FtoC(1));print(CtoF(-17.22))

#7C
from math import pi
gradeToRadian = lambda g: round(g*pi/180,2)
print(gradeToRadian(60))

#7D
perimeterOfSize = lambda sizes, length: sizes*length
print(perimeterOfSize(4, 2))

#7E
def listOf(cant):
    lista = []
    for i in range(cant): lista.append(input(f"Ingrese el elemento {i+1}: "))
    return lista
print(listOf(2))

#7F
def makeRectangle(h,w,char):
    for i in range(w):
        for j in range(h):
            print(char,end='')
        print()
makeRectangle(10,5,"#")

#7G
def makeTriangle(size):
    lista = []
    for i in range(size): lista.append("*")
    firstHalf(lista);lastHalf(lista)
def firstHalf(lista):
    for i in range( len(lista)-1 ): print("".join( lista[:i+1] ))
def lastHalf(lista):
    for i in range( len(lista) ): print("".join( lista[i:] ))
makeTriangle(4)
