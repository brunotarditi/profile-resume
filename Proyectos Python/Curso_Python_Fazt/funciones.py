#print()
#dir()
#type()

def hello(nombre = "Persona"):
    print("Hola " + nombre)

hello("Bruno")
hello()

def add(num1, num2):
    return num1 + num2

print(add(10,30))

suma = lambda n1, n2 : n1 + n2

print(suma(5,2))