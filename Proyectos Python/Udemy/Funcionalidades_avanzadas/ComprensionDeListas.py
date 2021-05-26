#Método tradicional
lista_trad = []
for letra in 'casa':
    lista_trad.append(letra)
print(lista_trad)

#Método de comprensión de listas
lista_comp = [letra for letra in 'casa']
print(lista_comp)

#Método tradicional
lista_num_trad = []
for numero in range(0,11):
    lista_num_trad.append(numero**2)
print(lista_num_trad)

#Método de comprensión de listas
lista_num_comp = [numero**2 for numero in range(0,11)]
print(lista_num_comp)

#Método tradicional
lista_par_trad = []
for numero in range(0,11):
    if numero % 2 == 0:
        lista_par_trad.append(numero)
print(lista_par_trad)

#Método de comprensión de listas
lista_par_comp = [numero for numero in range(0,11) if numero % 2 == 0]
print(lista_par_comp)

#Función anonima que simplifica

cuadrado = lambda numero: numero**2
print(cuadrado(4))

es_par = lambda par: par % 2 == 0
print(es_par(4))

