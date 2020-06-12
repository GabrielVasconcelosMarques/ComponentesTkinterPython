from tkinter import *

janela = Tk()
janela.geometry('300x200')


#Função criada para pegar o valor da primeira spinbox = s1
def getvalor():
    print(s1.get())


#Cria uma caixa de texto com setinha, onde tem valores que vao do numero 0 ate o 10
s1 = Spinbox(janela, from_=0, to=10)
s1.pack()

#Outro meio de atribuir valores ao spinbox, wrap, faz com que na setinha qd chegue ao valor maximo, ele resete e volte ao inicio
s2 = Spinbox(janela, values=(10, 20, 30, 40, 50), wrap=True)
s2.pack()

#Tambem pode passar parametros strings
s3 = Spinbox(janela, values=('Joao', 'Maria', 'Anastacia'))
s3.pack()

bt1 = Button(janela, text="Ver valor", command=getvalor)
bt1.pack()


janela.mainloop()