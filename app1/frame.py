from tkinter import *

janela = Tk()

#Definindo frames para melhor visualização de menus, atraves do frame conseguimos alocar elementos na mesma janela
frame_nome = Frame(janela)
frame_morada = Frame(janela)

#Definindo labels
lblNome = Label(frame_nome, text='Nome:')
lblApelido = Label(frame_nome, text='Apelido:')
lblRua = Label(frame_morada, text='Rua:')
lblCidade = Label(frame_morada, text='Cidade:')

#Definindo entrys
entry_nome = Entry(frame_nome)
entry_apelido = Entry(frame_nome)
entry_rua = Entry(frame_morada)
entry_cidade = Entry(frame_morada)

#Definindo botão
bt1 = Button(janela, text="Executar")

#Definindo o local do primeiro frame
lblNome.grid(row=0, column=0)
lblApelido.grid(row=1, column=0)
entry_nome.grid(row=0, column=1)
entry_apelido.grid(row=1, column=1)

#Definindo local do segundo frame
lblRua.grid(row=0, column=0)
lblCidade.grid(row=1, column=0)
entry_rua.grid(row=0, column=1)
entry_cidade.grid(row=1, column=1)

#Posicionando os frames
frame_nome.grid(row=0, column=0)
frame_morada.grid(row=0, column=1)

bt1.grid(column=1)


janela.mainloop()