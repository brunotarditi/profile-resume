from tkinter import *


#Configuración de la raíz
root = Tk()

#Label y Entry
label = Label(root,text="Nombre: ")
label.grid(row=0,column=0,sticky="w",padx=5,pady=5)

entry = Entry(root)
entry.grid(row=0,column=1)
entry.config(justify="center",state="disable")

label2 = Label(root,text="Apellido: ")
label2.grid(row=1,column=0,sticky="w",padx=5,pady=5)

entry2 = Entry(root)
entry2.grid(row=1,column = 1)
entry2.config(justify="right")

label3 = Label(root,text="Contraseña: ")
label3.grid(row=2,column=0,sticky="w",padx=5,pady=5)

entry3 = Entry(root)
entry3.grid(row=2,column=1)
entry3.config(show="*")

root.mainloop()