from tkinter import *
#Configuración de la raíz
root = Tk()

texto = Text(root)
texto.pack()
texto.config(width=30,height=10,font=("Arial",12),padx=5,pady=5,selectbackground="blue")

#Finalmente bucle de la aplicación
root.mainloop()