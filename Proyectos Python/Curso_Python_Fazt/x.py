usuario = "Bruno"
correcto = False

while (correcto == False):
    teclado = input("Ingrese nombre: ")
    if usuario == teclado:
        print("usuario creado")
        correcto=True
        break
    else:
        print("usuario incorrecto")
