from collections import Counter
l = [1,2,3,4,1,2,3,1,2,1]
print(Counter(l))
p = "palabra"
print(Counter(p))
animales = "gato perro canario perro canario perro"
print(Counter(animales))
animales.split()
print(Counter(animales.split()))
c = Counter(animales.split())
c.most_common()
l = [10,20,30,40,10,20,30,10,20,10]
c = Counter(l)
print(c.items())
print(c.keys())
print(c.values())
print(sum(c.values()))
print(list(c))
print(dict(c))
#d.most_common(l) ¡error! ahora es un diccionario normal
print(set(c)) #devuelve a un conjunto
d = {} #diccionario vacío
#d['algo'] ¡error! no existe esa clave en el diccionario
from collections import defaultdict
d = defaultdict(float)
print(d['algo'])
print(d)
d = defaultdict(str)
d['algo']
print(d)
d = defaultdict(object)
d['algo']
print(d)
n = {}
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'
print(n)
from collections import OrderedDict
n = OrderedDict()
print(n)
t = (20,40,60)
print(t[0])
from collections import namedtuple
Persona = namedtuple('Persona','nombre apellido edad')
p = Persona(nombre="Bruno",apellido="Tarditi",edad=27)
print(p.nombre)
print(p.apellido)
print(p.edad)
