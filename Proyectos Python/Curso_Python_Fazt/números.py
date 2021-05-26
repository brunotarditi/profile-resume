edad = input("Ingrese su edad: ")
if int(edad) < 18:
    print("Menor")
elif int(edad) > 18:
    print("Mayor")
elif int(edad) >= 100:
    print("Fallecido")
elif int(edad) < 0:
    print("No nacido")
else:
    print("Desconocido")