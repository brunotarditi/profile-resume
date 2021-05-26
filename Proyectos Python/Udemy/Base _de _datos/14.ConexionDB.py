import sqlite3
conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

#cursor.execute("CREATE TABLE usuario(nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
#cursor.execute("INSERT INTO usuario VALUES ('Bruno Tarditi',28, 'brunotarditi@ejemplo.com')")

#cursor.execute("SELECT * FROM USUARIO")
#usuario = cursor.fetchone()
#print(usuario[2])

"""usuarios = [

    ('Camila',26,'camila@ejemplo.com'),
    ('Richard',4,'richard@ejemplo.com'),
    ('Ana',72,'Ana@ejemplo.com'),
]

cursor.executemany("INSERT INTO USUARIO VALUES (?,?,?)", usuarios)"""

cursor.execute("SELECT * FROM USUARIO")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)


conexion.commit()
conexion.close()
