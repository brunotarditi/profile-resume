from io import open
import pickle

class Pelicula:

    #Contructor de la clase
    def __init__(self,titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula: ",self.titulo)

    def __str__(self):
        return '{}({})'.format(self.titulo,self.lanzamiento)

class Catalogo:

    peliculas = []
    # Constructor de la clase

    def __init__(self):
        self.cargar()

    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catalogo está vacío")
            return
        for p in self.peliculas:
            print(p)

    def cargar(self):
        fichero = open('catalogo.pckl', 'ab+')
        fichero.seek(0)

        try:
            self.peliculas = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} peliculas".format(len(self.peliculas)))

    def guardar(self):
        fichero = open('catalogo.pckl', 'wb')
        pickle.dump(self.peliculas,fichero)
        fichero.close()

    #Destructor de la clase
    def __del__(self):
        self.guardar()
        print("Se ha guardado el fichero.")

c = Catalogo()
c.mostrar()
c.agregar(Pelicula("Star Wars IV", 150, 1977))
c.agregar(Pelicula("Star Wars V", 162, 1980))
del(c)
c = Catalogo()
c.mostrar()
del(c)
c = Catalogo()
c.agregar(Pelicula("Star Wars VI", 180, 1983))
c.mostrar()
del(c)
c = Catalogo()
