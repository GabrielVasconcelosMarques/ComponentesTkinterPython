from tkinter import *

janela = Tk()
janela.geometry('300x200')

#Comando para criar menu
meuMenu = Menu(janela)

#Função para definição de comando
def filenew():
    print("File new")

#Criação dos Submenus, que aparecem dentro das guias do menu, o tearoff é para tirar a opçao do submenu de arrastar a janela
#Definindo comandos
fileMenu = Menu(meuMenu, tearoff=0)
fileMenu.add_command(label="New", command=filenew)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save as")
#Adiciona um separador no menu
fileMenu.add_separator()
fileMenu.add_command(label='Exit')

#Criação da guia principal do menu, e definindo as subguias a ela
meuMenu.add_cascade(label="File", menu=fileMenu)


#Criação do menu open (submenus)
editMenu = Menu(meuMenu, tearoff=0)
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")
editMenu.add_command(label="Cut")
editMenu.add_command(label="Find")
#Criação do menu open (principal)
meuMenu.add_cascade(label="Edit", menu=editMenu)


#Modo de colocar o menu na janela, como se fosse um pack
janela.config(menu=meuMenu)


janela.mainloop()