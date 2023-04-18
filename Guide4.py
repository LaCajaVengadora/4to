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
#3F
#3G
#3H
#3I
#3J
#3K
#3L
#3M
#3N
#3Ñ
#3O
