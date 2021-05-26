#Generadores
def pares(n):
    for numero in range(n+1):
        if numero % 2 == 0:
            yield numero #ceder numero

for numero in pares(10):
    print(numero)

#Iteradores
lista = [1,2,3,4,5]
lista_iterable = iter(lista)
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))