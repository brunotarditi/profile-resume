from tkinter import *

def seleccionar():
    cadena = ""
    if(leche.get()):
        cadena += "Con leche"
    else:
        cadena += "Sin leche"

    if (azucar.get()):
        cadena += " y con azúcar"
    else:
        cadena += " y sin azúcar"

    monitor.config(text = cadena)


root = Tk()
root.title('Cafetería')
root.config(bd=15)

leche = IntVar()
azucar = IntVar()

frame = Frame(root)
frame.pack(side = "left")
Label(root, text = "¿Cómo quieres el café?").pack(anchor = 'w')
Checkbutton(root, text = "Con leche", variable = leche, onvalue = 1, offvalue = 0, command = seleccionar).pack(anchor = 'w')
Checkbutton(root, text = "Con azúcar", variable = azucar, onvalue = 1, offvalue = 0, command = seleccionar).pack(anchor = 'w')

monitor = Label()
monitor.pack()








root.mainloop()