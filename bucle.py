import random

Secreto = random.randint(1,10)

Numero = int (input("Adivine el numero entre 1 y 10"))

while Numero != Secreto:
    if Numero < Secreto:
        print ("El numero es mayor")
    else:
        print  ("El numero es menor")

    Numero = int (input("Intenta de nuevo"))

print ("Felicidades adivinaste el numero", Secreto)
