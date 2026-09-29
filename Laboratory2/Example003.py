#Contador de estrella---- utilizando bucles y creatividad--

star = 100
import time 
import random

user = int(input("¿cuanta estrella quiere ver?: "))
#se crea el bucle for 
for star in range (user):
    
    space = " "  * random.randint(1,50)
    # Se imprime los espacio y la estrella

    print(f"{space} ✨ number star{ star + 1} turn on")
    #en esta parte se pausa el programa 
    time.sleep (0.10)

print("\n ✨tu cielo esta lleno de estrella ⭐✨")



