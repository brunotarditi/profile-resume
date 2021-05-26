
numeros = [2, 6, 15, 20, 25, 38, 50]

print(list(filter(lambda numero: numero % 5 == 0, numeros)))

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} de {self.edad} años."

personas = [
    Persona('Marcelo', 28),
    Persona('Richard', 5),
    Persona('Lorena', 58)
]

menores = filter(lambda persona: persona.edad < 18, personas)
for menor in menores:
    print(menor)