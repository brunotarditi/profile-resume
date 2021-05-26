import sqlite3
#Crear conexión
miConexion = sqlite3.connect("GestionProductos.db")
#Crear puntero
miCursor = miConexion.cursor()
#Crear una tabla para mi base de datos
"""miCursor.execute('''
CREATE TABLE PRODUCTOS(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NOMBRE VARCHAR(50),
PRECIO REAL)
''')

productos = [
    ("televisor", 36.999),
    ("arróz", 55.20)
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?)",productos)"""

miConexion.commit()

miConexion.close()

"""#Añadir productos
productos = [
    ("televisor", "electrónica"),
    ("leche", "lacteos"),
    ("bola de lomo", "carnes"),
    ("remera", "ropa")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?)", productos)
#miCursor.execute("INSERT INTO PRODUCTOS VALUES (NULL, 'pantalón', 'ropa')")
miCursor.execute("SELECT * FROM PRODUCTOS WHERE CATEGORIA = 'ropa'")
miCursor.execute("UPDATE PRODUCTOS SET CATEGORIA = 'televisores' where NOMBRE_ARTICULO = 'televisor'")
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 5")

productos = miCursor.fetchall()
print(productos)

miCursor.execute("SELECT * FROM CATEGORIA")
variasCategorias = miCursor.fetchall()
for categoria in variasCategorias:
    print(categoria)
"""
