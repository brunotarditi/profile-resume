def monitorizar_args(funcion):

    def decorar(*args, **kwargs):
        print("\t *Se está a punto de ejecutar a la función:", funcion.__name__)

        funcion(*args, **kwargs)

        print("\t *Se está a punto de finalizar a la función:", funcion.__name__)

    return decorar

@monitorizar_args
def hola(nombre):
    print(f"hola {nombre}")

@monitorizar_args
def adios(nombre):
    print(f"adios {nombre}")

hola('Bruno')
print()
adios('Bruno')


