from tkinter import *

janela = Tk()
janela.title("Janela")

#O get pega o que o usuario digitou no entry
def executar():
    lbl1['text'] = e1.get()
    lbl2['text'] = e2.get()
    lbl3['text'] = e3.get()

#Criando entrys
e1 = Entry(janela)
e2 = Entry(janela)
e3 = Entry(janela)

e1.grid()
e2.grid()
e3.grid()

#criando labels
lbl1 = Label(janela)
lbl2 = Label(janela)
lbl3 = Label(janela)

lbl1.grid()
lbl2.grid()
lbl3.grid()

#Criando botões
bt1 = Button(janela, text="Executar", command=executar)
bt1.grid()

#Coloca o cursor piscando no primeiro entry
e1.focus()



janela.mainloop()