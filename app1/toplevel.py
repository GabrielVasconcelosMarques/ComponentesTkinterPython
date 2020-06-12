from tkinter import *

janela = Tk()
janela.geometry("300x200")


#Função criada para abrir o toplevel, uma nova janela a parte
def abrir_top():
    #Criando um top level
    top = Toplevel()
    top.title("Novo formulário")
    top.geometry('200x200')
    lbl = Label(top, text="Esse é o novo formulario")
    lbl.pack()

bt1 = Button(janela, text="Abrir novo", command=abrir_top)
bt1.pack()

janela.mainloop()