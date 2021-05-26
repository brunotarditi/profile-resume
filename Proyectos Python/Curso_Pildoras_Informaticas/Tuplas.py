#Tupla creada
mi_tupla = ("Pepe",5,True,6.5)
#Tupla mostrada
print(mi_tupla)
#Convertir mi tupla a lista
mi_lista = list(mi_tupla)
print(mi_lista)
#convertir una lista a tupla
mi_tupla_uno = tuple(mi_lista)
print(mi_tupla_uno)

#Buscar elemento en la tupla
print("Pepe" in mi_tupla_uno)

#otra forma de buscar
print(mi_tupla_uno.count("Pepe"))

#Averiguar la longitud de la tupla
print(len(mi_tupla_uno))

#Tupla unitaria
tupla_unitaria = ("Pepe",)
print(len(tupla_unitaria))

nombre, numero, booleano, flotante = mi_tupla_uno
print(nombre)
print(numero)
print(booleano)
print(flotante)