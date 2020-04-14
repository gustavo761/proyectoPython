import tkinter as tk
root = tk.Tk()

def sumar():
    a = float(numero1.get())
    b = float(numero2.get())
    resultado.set(str(a+b))
    numero1.set('')
    numero2.set('')

def restar():
    a = float(numero1.get())
    b = float(numero2.get())
    resultado.set(str(a-b))
    numero1.set('')
    numero2.set('')

def multiplicar():
    a = float(numero1.get())
    b = float(numero2.get())
    resultado.set(str(a*b))
    numero1.set('')
    numero2.set('')

def dividir():
    a = float(numero1.get())
    b = float(numero2.get())
    resultado.set(str(a/b))
    numero1.set('')
    numero2.set('')

root.geometry('500x230')
root.title('Calculadora')
root.configure(bg="#009688")

numero1 = tk.StringVar()
numero2 = tk.StringVar()
resultado = tk.StringVar()
a = 50
b = 50
tk.Label(root, text='CALCULADORA', bg="#009688", fg='white', font=('',20)).place(x=150, y=20)

tk.Label(root, text='Número 1:', bg='#009688', fg='white', font=('',15)).place(x=a-10,y=b+10)
tk.Entry(root, justify='center', textvariable=numero1).place(x=a+90,y=b+15)
tk.Button(root, text='Sumar', width=10, bd=0, command=sumar).place(x=a+250, y=b+13)
tk.Button(root, text='Restar', width=10, bd=0, command=restar).place(x=a+330, y=b+13)

tk.Label(root, text='Número 2:', bg='#009688', fg='white', font=('',15)).place(x=a-10,y=b+55)
tk.Entry(root, justify='center', textvariable=numero2).place(x=a+90,y=b+60)
tk.Button(root, text='Multiplicar', width=10, bd=0, command=multiplicar).place(x=a+250,y=b+58)
tk.Button(root, text='Dividir', width=10, bd=0, command=dividir).place(x=a+330,y=b+58)

tk.Label(root, text='resultado:', bg='#009688', fg='white', font=('',15)).place(x=a-10,y=b+100)
tk.Label(root, textvariable=resultado, bg='#009688', fg='white', font=('',15)).place(x=a+90,y=b+100)

tk.Button(root, text='Salir', bd=0, command=root.destroy, width=10).place(x=a+250, y=b+103)

root.mainloop()