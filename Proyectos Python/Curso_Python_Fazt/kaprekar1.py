#Pido un número
numero = input("Ingrese un número de 4 cifras las cuales no sean todas iguales: ")
print("Se ingresa el número: ",numero)
n = int(numero)
ordenado = numero
while True:
    ordenado = int(numero)
    for i in range(10):
        ordenado = "{:04d}".format(n)
        mayorMenor = "".join(sorted(ordenado, reverse=True))
        menorMayor = "".join(sorted(ordenado))
        n = int(mayorMenor) - int(menorMayor)
        if n == 0:
            numero = input("Ingrese un número de 4 cifras las cuales no sean todas iguales: ")
            n = int(numero)
    if n == 6174:
        break
n = int(numero)
for i in range(10):
    numero = "{:04d}".format(n)
    mayorMenor = "".join(sorted(numero, reverse = True))
    menorMayor = "".join(sorted(numero))
    n = int(mayorMenor) - int(menorMayor)
    print(mayorMenor,"-", menorMayor,"=", n, "iteración: ({:1d})".format(i + 1))
    if n == 0:
        break
    if n == 6174:
        break
print("-----------------------------------")
print("La constante de Kaprekar es:","'",n,"'","se logró con", i+1, "iteraciones.")