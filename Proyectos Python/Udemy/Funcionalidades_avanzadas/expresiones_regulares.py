import re

texto = "Sic Mundus Creatus Est"
print(re.search("Mundus", texto))

palabra = "Mundus"
encontrado = re.search(palabra, texto)

if encontrado:
    print("Se ha encontrado.")
else:
    print("No se ha encontrado.")

#Donde empieza la palabra
print(encontrado.start())
#Donde termina
print(encontrado.end())
#Empieza y termina
print(encontrado.span())
#Recuperamos la frase
print(encontrado.string)
#Busca un patrón al principio de la cadena
print(re.match("Sic", texto))
#Sirve para dividir una cadena a partir de un patron
print(re.split(' ', texto))
#Sustituye todas las coincidencias
print(re.sub('Creatus', 'Tic Tac', texto))
#Buscar todas las coincidencias
otro_texto = 'hola, adios, hola, hola'
print(re.findall('hola', otro_texto))

#Metacaracteres

palabra_hola = 'hla, hola, hoola, hooola, hooooooola'


def buscar_patron(patrones, palabra_hola):

    for patron in patrones:
        print(re.findall(patron, palabra_hola))


patrones = ['ho*', 'ho+', 'ho?', 'ho{3}'] # * → 0 o más repeticiones, + → 1 o más, ? → una o ninguna, {} → las que queramos
buscar_patron(patrones, palabra_hola)



