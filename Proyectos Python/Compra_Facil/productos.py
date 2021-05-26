from tkinter import ttk
from tkinter import *
import sqlite3


class Product:
    db_name = 'GestionProductos.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Compra Fácil')

        # Crear contenedor Frame
        frame = LabelFrame(self.wind, text='Registrar un nuevo producto')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Ingresa un nombre
        Label(frame, text='Nombre: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        # Ingresa un precio
        Label(frame, text='Precio: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        # Botón para agregar producto
        ttk.Button(frame, text='Guardar Productos', command = self.add_product).grid(row=3, columnspan=2, sticky = W + E)

        # Mensaje saliente
        self.mensaje = Label(text = '', fg = 'red' )
        self.mensaje.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        # Tabla
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='Precio', anchor=CENTER)

        # Botón
        ttk.Button(text = 'Eliminar', command = self.delete_product).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(text='Editar', command = self.edit_product).grid(row=5, column=1, sticky=W + E)

        # Lenando las filas de la talba

        self.get_products()

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_products(self):

        # limpiando tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        # Consultando datos
        query = 'SELECT * FROM PRODUCTOS ORDER BY NOMBRE DESC'
        db_rows = self.run_query(query)

        # llenando datos
        for row in db_rows:
            print(row)
            self.tree.insert('', 0, text = row[1], values = row[2])

    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO PRODUCTOS VALUES(NULL,?,?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.mensaje['text'] = 'El producto {} ha sido actualizado'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.mensaje['text'] = 'El nombre y el precio son requeridos'
        self.get_products()

    def delete_product(self):
        self.mensaje['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text'] = 'Por favor selecciona un registro'
            return
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM PRODUCTOS WHERE NOMBRE = ?'
        self.run_query(query, (name, ))
        self.mensaje['text'] = 'El registro {} ha sido eliminado'.format(self.name.get())
        self.get_products()

    def edit_product(self):
        self.mensaje['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text'] = 'Por favor selecciona un registro'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Editar productos'

        # Nombre anterior
        Label(self.edit_wind, text = 'Nombre anterior: ').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state = 'readonly').grid(row = 0, column = 2)

        # Nombre nuevo
        Label(self.edit_wind, text = 'Nombre nuevo').grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)

        # Precio anterior
        Label(self.edit_wind, text = 'Precio anterior: ').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row = 2, column = 2)

        # Precio nuevo
        Label(self.edit_wind, text = 'Precio nuevo').grid(row = 3, column = 1)
        new_price = Entry(self.edit_wind)
        new_price.grid(row = 3, column = 2)

        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row = 4, column = 2, sticky = W)

    def edit_records(self, new_name, name, new_price, old_price):
        query = 'UPDATE PRODUCTOS SET NOMBRE = ?, PRECIO = ? WHERE NOMBRE = ? AND PRECIO = ?'
        parameters = (new_name, new_price, name, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.mensaje['text'] = 'El registro {} ha sido actualizado'.format(name)
        self.get_products()

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
