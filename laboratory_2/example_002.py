#aAdivinando el numero-- Utilizando bucles y condiciones--

import random


number_secret = random.randint(1,20)

tried = int(input("Adivina el numero (entre 1 al 20)"))

while tried != number_secret: 
    
 if tried < number_secret:
    print("Numero muy bajo, intentalo de nuevo")
    tried = int(input("Adivina el numero: "))
 else:
    print("Numero muy alto, sigue intentandolo")
    tried = int(input("Adivina el numero: "))  
    
print("Felicidades, Adivinaste el numero correcto")