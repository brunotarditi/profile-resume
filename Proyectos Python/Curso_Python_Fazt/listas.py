demo_list = [1, 'hola',1.2,True,[1,2,3]]
colores = ['rojo', 'azul', 'amarillo']

lista_numeros = list((1,2,3,4))
print(lista_numeros)

rango =  list(range(1, 11))
print(rango)
#Métodos para listas
#print(dir(colores))
print(len(colores))
print(colores.pop())
print('rojo' in colores)
colores.append('negro')
print(colores)
colores.extend(['violeta','blanco'])
print(colores)

#color.insert(-1, 'naranja')
colores.insert(len(colores), 'naranja')


colores.sort()
print(colores)