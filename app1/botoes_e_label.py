from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primeiro app")
menu_inicial.geometry("700x700")


#Criando função para um botao, na função eu usei um parametro, logo no command do botao, deverá ser utilizado o lambda
def click(mensagem):
    print(mensagem)

#Criando função para o botão. função sem parametro, não utiliza lambda no comando
def click2():
    print("Olá mundo2")

#Criando botão com passagem de argumento atraves do lambd
bt1 = Button(menu_inicial, text="Executar", command=lambda: click("Olá mundo"))
bt1.pack()

#Criando botao sem passagem de argumento
bt2 = Button(menu_inicial, text="Iniciar", command=click2)
bt2.pack()

#Criando label width é largura e height é altura
lbl1 = Label(menu_inicial, text="Esse é o label 1", bg="yellow", fg="red", font="Times", width=20, height=10)
lbl1.pack()

#Na fonte podemos definir o tipo de fonte, tamanho, negrito, italico
lbl2 = Label(menu_inicial, text="Esse é o label 2", bg="green", fg="brown", font="arial 10 bold italic")
lbl2.pack()

#O bd junto com o relief cria uma borda solida ao redor da lbl, o bd tem a ver com a espessura
#tipos de relief = solid, flat, raised, sunken, ridge, groove
lbl3 = Label(menu_inicial, text="Esse é o label 3", font="arial 20", bd=1, relief="solid")
lbl3.pack()

#O anchor é utilizado para alinhamento do texto, o parametro passado smpre deve ser maisculo,e nao coloca entre aspas
#N=norte, S=sul, W=oeste, E=leste, NW, SE, pode se fazer combinações, e para centralizar usa CENTER
#padx e pady sao as distancias das bordas ate a letra 
lbl4 = Label(menu_inicial, text="Esse é o label 4", font="arial 20", anchor=N,bd=1, relief='solid', padx=50, pady=50)
lbl4.pack()

#Justify alinha o texto a direita, esquerda ou centro = LEFT, RIGHT, CENTER, deve ser sempre usado com o anchor
lbl5 = Label(menu_inicial, text="EUm texto\nmais um texto\nteste", font="arial 20", anchor=N,bd=1, relief='solid', justify=LEFT)
lbl5.pack()

#O stick é usado para alinhamento, baseado na rosa dos ventos
lbl6 = Label(menu_inicial, text="label 6:")
#lbl6.grid(row=0, stick=W)



menu_inicial.mainloop()