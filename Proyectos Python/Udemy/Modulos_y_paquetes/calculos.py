from Udemy.Modulos_y_paquetes import operaciones

a, b, c, d, = 10, 5, 0, "hola"

print(f"{a} + {b} = {operaciones.suma(a,b)}")
print(f"{b} - {d} = {operaciones.resta(b,d)}")
print(f"{b} * {b} = {operaciones.multiplicacion(b,b)}")
print(f"{a} / {c} = {operaciones.division(a,c)}")
