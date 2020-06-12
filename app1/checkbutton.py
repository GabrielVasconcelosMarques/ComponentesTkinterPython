from tkinter import *

janela = Tk()

def apresentar():
    print(valor_check.get())

#Criando variavel do tipo inteiro
valor_check = IntVar()

#Criando um checkbutton, atribuindo que sua variavel é uma variavel inteira, quando esta marcada retorna 1
check = Checkbutton(janela, text='Esta é uma checkbox', variable=valor_check, command=apresentar, font='arial 20')
check.pack()

janela.mainloop()