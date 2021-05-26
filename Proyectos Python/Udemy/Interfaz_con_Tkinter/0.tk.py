from tkinter import *

root = Tk()
root.title("Facebook")
root.resizable(1,1)
root.iconbitmap('facebook.ico')


frame = Frame(root, width=480,height=320)
frame.pack(fill='both',expand=1)
frame.config(cursor="spider")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")


root.config(cursor="arrow")
root.config(bg="red")
root.config(bd=15)
root.config(relief="ridge")

label = Label(frame, text = "¡Hola mundo!")
label.pack(anchor="center")
label.config(bg="blue",fg="yellow",font=("Arial",24))


#Finalmente bucle de la aplicación
root.mainloop()