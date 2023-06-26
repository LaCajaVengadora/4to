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
