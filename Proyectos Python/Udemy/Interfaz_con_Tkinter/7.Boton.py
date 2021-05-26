from tkinter import *

def sumar():
    result.set(float(n1.get()) + float(n2.get()))
    borrar()
def restar():
    result.set(float(n1.get()) - float(n2.get()))
    borrar()

def multiplicar():
    result.set(float(n1.get()) * float(n2.get()))
    borrar()

def borrar():
    n1.set("")
    n2.set("")

root = Tk()
root.config(bd = 15)

n1 = StringVar()
n2 = StringVar()
result = StringVar()
Label(root, text = "Número 1:").pack()
Entry(root, justify = 'center', textvariable = n1).pack()
Label(root, text = "Número 2:").pack()
Entry(root, justify = 'center', textvariable = n2).pack()
Label(root, text = "Resultado:").pack()
Entry(root, justify = 'center', textvariable = result, state = 'disable').pack()
Label(root, text = '').pack()
Button(root, text = 'Suma', command = sumar).pack(side='left')
Button(root, text = 'Resta', command = restar).pack(side = 'left')
Button(root,text = 'Multiplicación', command = multiplicar).pack(side='left')


root.mainloop()



