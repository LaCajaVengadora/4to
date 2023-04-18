#4B
from random import choice
elc = input("Elige 'cara' o 'ceca'").lower()
print("Ha salido", end=" "); 
value = choice(("cara", "ceca")); print(value)
if elc == value: print("Ganaste")
else: print("Perdiste")
  
#3C
from random import c randrange
n = int(input("Elige un numero entre 0 y 10 (más facil asi)")); 
trueN = randrange(1,11)
if n==trueN: print(f"Correcto, era {n}")
else: print(f"Incorrecto, era {trueN}")
  
#3D
from random import randint
nT = randint(1,6); print(f"Tomás ha sacado {nT}")
nL = randint(1,6); print(f"Lucia ha sacado {nL}")
if nT<nL: print("Ha ganado Lucia")
elif nT>nL: print("Ha ganado Tomás")
else: print("Empataron")
  
#3E
from random import randint

def getMax(a,b):
    if a>b: return a
    elif a<b: return b
    else: return 0
    
O1 = randint(1,6); O2 = randint(1,6); print(f"Oriana ha sacado {O1} y {O2}, siendo el total {O1+O2}")
J1 = randint(1,6); J2 = randint(1,6); print(f"Julian ha sacado {J1} y {J2}, siendo el total {J1+J2}")
if O1+O2>J1+J2: print("Ha ganado Oriana")
elif O1+O2<J1+J2: print("Ha ganado Julian")
elif getMax(O1,O2)>getMax(J1,J2): print("Ha ganado Oriana")
elif getMax(O1,O2)<getMax(J1,J2): print("Ha ganado Julian")
else: print("Empate")
  
#3F
from random import randint
def getMax(a,b): ...
def getMin(a,b): ...
H1 = randint(1,6); H2 = randint(1,6); print(f"Helena ha sacado {H1} primero y luego {H2}")
N1 = randint(1,6); N2 = randint(1,6); print(f"Nehuen ha sacado {N1} primero y luego {N2}")
if getMax(H1,H2)>getMax(N1,N2): print("Ha ganado Helena")
elif getMax(H1,H2)<getMax(N1,N2): print("Ha ganado Nehuen")
elif getMin(H1,H2)>getMin(N1,N2): print("Ha ganado Helena")
elif getMin(H1,H2)<getMin(N1,N2): print("Ha ganado Nehuen")
else: print("Empate")
  
#3G
from random import randint
E1 = randint(1,10); E2 = randint(1,10); E3 = randint(1,10)
print(f"Evangelina ha sacado {E1} , {E2} y {E3}"); allE = E1+E2+E3
S1 = randint(1,10); S2 = randint(1,10); S3 = randint(1,10); allS = S1+S2+S3
print(f"Simon ha sacado {S1} , {S2} y {S3}")
if allS>15 and allE>15: print("Empate, ambos se pasaron")
elif allE>15: print("Gana Simon")
elif allS>15: print("Gana Evangelina")
elif allS>allE: print("Gana Simon")
elif allS<allE: print("Gana Evangelina")
else: print("Empate, sacaron lo mismo")
  
#3H
from random import choice
userPick = input("Ingrese piedra, papel o tijeras").lower()
randomPick = choice(("piedra", "papel", "tijeras")); print(randomPick)
if userPick==randomPick: print("Empate")
elif userPick=="tijeras":
    if randomPick=="piedraa": print("Perdiste")
    else: print("Ganaste")
elif userPick=="piedra":
    if randomPick=="papel": print("Perdiste")
    else: print("Ganaste")
elif userPick=="papel":
    if randomPick=="tijeras": print("Perdiste")
    else: print("Ganaste")
else: print("PIEDRA , PAPEL o TIJERAS")
  
#3I
from random import choice
userPick = input("Ingrese piedra, papel, tijeras, lagarto o spock").lower()
randomPick = choice(("piedra", "papel", "tijeras", "lagarto", "spock")); print(randomPick)

if userPick==randomPick: print("Empate")
elif userPick=="tijeras":
    if randomPick=="piedra" or randomPick=="spock": print("Perdiste")
    else: print("Ganaste")
elif userPick=="piedra":
    if randomPick=="papel" or randomPick=="spock": print("Perdiste")
    else: print("Ganaste")
elif userPick=="papel":
    if randomPick=="tijeras" or randomPick=="lagarto": print("Perdiste")
    else: print("Ganaste")
elif userPick=="lagarto":
    if randomPick=="tijeras" or randomPick=="piedra": print("Perdiste")
    else: print("Ganaste")
elif userPick=="spock":
    if randomPick=="papel" or randomPick=="lagarto": print("Perdiste")
    else: print("Ganaste")
else: print("PIEDRA , PAPEL , TIJERAS , LAGARTO o SPOCK")
#3J YA HECHO
#3K
#3L
#3M
#3N
#3Ñ
#3O
