from tkinter import *

janela = Tk()

lista = Listbox(janela)
lista.pack()

#Função criada para mostrar no console os elemntos que estao sendo clicados na listbox, que estao ativos
def executar():
    print(lista.get(ACTIVE))

#Inserir elementos na listbox

#Insere o nome primeiro texto, sempre ao final da listbox
'''lista.insert(END, "Primeiro texto")

#Ou pode determinar o indice a inserir
lista.insert(0, "Primeiro texto")
lista.insert(1, "Primeiro texto")
lista.insert(2, "Primeiro texto")'''

#Pode adicionar tbm atraves de listas e for
nomes = ['Gabriel', 'Rayssa', 'Rejane', 'Valeria', 'igor', 'feijó', 'quencio', 'lancia', 'pristico', 'major', 'soldado', 'ana', 'joaquim']
for nome in nomes:
    lista.insert(END, nome)

bt1 = Button(janela, text="Clique", command=executar)
bt1.pack()

janela.mainloop()