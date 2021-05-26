def suma(a, b):
    try:
        result =  a + b
    except TypeError:
        print("Error, tipo de dato no válido.")
    else:
        return result

def resta(a, b):
    try:
        result = a - b
    except TypeError:
        print("Error, tipo de dato no válido.")
    else:
        return result

def multiplicacion(a, b):
    try:
        result = a * b
    except TypeError:
        print("Error, tipo de dato no válido.")
    else:
        return result

def division(a, b):
    try:
        result = a / b
    except TypeError:
        print("Error: tipo de dato no válido.")
    except ZeroDivisionError:
        print("Error: no es posible dividir por cero.")
    else:
        return result