#Se importa librería random
from random import randint, uniform, random 

#Variables

intentos = 10
numeroSecreto = randint(1, 100)
numIngresado = 0

#Código
print("Adivina el número secreto (de 1 a 100)")
numIngresado = int(input("Ingrese un número: "))
while ((numIngresado != numeroSecreto) and (intentos > 0)):
    if(numIngresado < numeroSecreto):
        print("Es muy bajo.")
    else:
        print("Es muy alto.")
    if(intentos == 1):
        break
    intentos = (intentos - 1)
    print(f"Le quedan " + format(intentos) + " intentos. Ingrese otro número.")
    numIngresado = int(input("Ingrese un número: "))
if(numeroSecreto == numIngresado):
    print(f"¡Exacto! Usted adivinó en " + format(intentos) + " intentos.")
else:
    print(f"El número era: " + format(numeroSecreto))

