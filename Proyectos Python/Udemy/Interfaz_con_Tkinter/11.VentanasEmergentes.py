from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()
root.config(bd=15)


def test():

    # MessageBox.showinfo("Hola!","Hola Mundo")
    # MessageBox.showwarning("Alerta","Sin chistes que me arrepiento y lo cambio.")
    # MessageBox.showerror("Error", "Aunque no lo parezca, es domingo, mañana lo veo.")
    resultado = MessageBox.askquestion("Hola","¿Mañana nos juntamos?")
    if resultado == 'yes':
        root.destroy()

    """resultado = MessageBox.askokcancel("Salir", "¿Sobreescribir el fichero actual?")
    if resultado:
        root.destroy()"""

    """resultado = MessageBox.askyesno("Salir", "¿Estás seguro que desea salir sin guardar?")
    if resultado:
        root.destroy()"""

    """resultado = MessageBox.askretrycancel("Reintentar", "No se puede conectar")
    if resultado:
        root.destroy()"""

Button(root, text= "Clic", command = test).pack()






root.mainloop()