#Conversor de temperatura fehrenheit para celsius

from tkinter import *

janela = Tk()
janela.title("Conversor de temperatura")

def calcular():
    f = float(e1.get())
    c = (f - 32) * 5/9
    lbl2['text'] = "{:.1f}° celsius".format(c)


lbl1 = Label(janela, text="Digite aqui a temperatura em Fahrenheit \na ser convertida para Celsius: ", justify=LEFT, font="arial 20")
e1 = Entry(janela, font='arial 20')
lbl2 = Label(janela, font="arial 20")
bt1 = Button(janela, text="Converter", command=calcular, font="arial 20", bd=5, relief="raised")

lbl1.grid()
e1.grid()
lbl2.grid()
bt1.grid(stick=E)


janela.mainloop()

