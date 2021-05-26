
class Persona:
    nombre = ''

miLista = ["Juan", 5, "Richard", 1.2]

print(miLista[:]) #muestra toda la lista
print(miLista[-2]) #muestra por posición
print(miLista[0:2]) #muestra un trozo de la lista


miLista.append(25) #agrega un elemento al final de la lista
miLista.insert(2,35) #agrega un elemento en la posición que uno quiera

print(miLista[:])

nuevaPersona = Persona()
nuevaPersona.nombre = "Bruno"
miLista.extend([False, "Agustina",15.2,nuevaPersona.nombre]) #se agregan varios elementos a la lista

print(miLista)
print(miLista.index(False))
print("agustina" in miLista)

miLista.remove(False) #remueve el elemento a indicar

print(miLista)

miLista.pop() #elimina el último elemento de la lista

print(miLista)

miLista2 = [45,"Sandra","Lucia",27]

miLista3 = miLista + miLista2

print(miLista3)



