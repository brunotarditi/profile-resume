from tkinter import *
#Configuración de la raíz
root = Tk()

#Variable dinámica
texto = StringVar()
texto.set("Un nuevo texto")

#Configuración de un marco
frame = Frame(root, width = 480, height = 320)
frame.pack()
#Configuración de la etiqueta
label = Label(frame, text = "¡Hola Mundo!")
label.place(x=100, y=100)
label.config(textvariable = texto)

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen,bd=0).pack()

root.mainloop()