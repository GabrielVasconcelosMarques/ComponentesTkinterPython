from tkinter import *

janela = Tk()

frameA = Frame(janela)
frameB = Frame(janela)

#Varia vel criada para ser passada por parametro para a variable no radiobutton, assim o usuario so pode selecionar uma opção dentre as
# fornecidas
valor_a = IntVar()

#Função criada para o comando do ra_1
def comando_ra_1():
    print('Opção 1')

#Criação de radiobuttons, cada uma deve ter um value diferente e a variable atribuida a uma variavel, para o usuario conseguir
# marcar apenas uma alternativa, eles tbm podem apresentar comando, como mostra o ra_1
ra_1 = Radiobutton(frameA, text='Opção A', variable=valor_a, value=1, command=comando_ra_1)
ra_2 = Radiobutton(frameA, text='Opção B', variable=valor_a, value=2)
ra_3 = Radiobutton(frameA, text='Opção C', variable=valor_a, value=3)

ra_1.grid()
ra_2.grid()
ra_3.grid()

valor_b = IntVar()

ra_4 = Radiobutton(frameB, text='Opção D', variable=valor_b, value=4)
ra_5 = Radiobutton(frameB, text='Opção E', variable=valor_b, value=5)
ra_6 = Radiobutton(frameB, text='Opção F', variable=valor_b, value=6)

ra_4.grid()
ra_5.grid()
ra_6.grid()

frameA.grid(row=0, column=0)
frameB.grid(row=0, column=1)

#Essa função faz com que o ra_1 venha automaticamente marcado
ra_1.select()
ra_4.select()

#Função criada para ver o valor selecionado pelo raddiobutton
def ver_radio_valor():
    print(valor_a.get())

bt1 = Button(janela, text="Executar", command=ver_radio_valor)
bt1.grid(row=2, column=1)

janela.mainloop()