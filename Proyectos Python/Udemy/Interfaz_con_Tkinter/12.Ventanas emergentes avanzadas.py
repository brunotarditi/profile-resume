from tkinter import *
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()
root.config(bd=15)

def test():

    """color = ColorChooser.askcolor(title = "Elige un color")
    print(color)"""

    """ruta = FileDialog.askopenfilename(title = "Abrir un fichero", initialdir = "D:", filetypes = (("Fichero de texto", "*.txt"),
                                                                                                  ("Fichero de texto avanzados", "*.txt2"),
                                                                                                  ("Todos los ficheros", "*.*")))
    print(ruta)"""

    fichero = FileDialog.asksaveasfile(title = "Guardar un fichero", mode = "w", defaultextension = ".txt")
    if fichero is not None:
        fichero.write("Hola este es un fichero de prueba")
        fichero.close()




Button(root, text= "Clic", command = test).pack()

root.mainloop()