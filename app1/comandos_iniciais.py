from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primeira aplicação")

#os dois primeiros sao dimensao, os dois posteriores são onde a janeça iniciará
menu_inicial.geometry("400x400+200+200") 

#Faz com que a janela não seja redimensionada, atraves de altura e largura
menu_inicial.resizable(True, True)

#defini o tamanho minimo que a janela pode ter, nao pode ser menor que isso
menu_inicial.minsize(400, 400)

#defini o tamanho maximo que a janela pode ter, nao pode ser maior que isso
menu_inicial.maxsize(700, 700)

#Faz com que a janela seja iniciada em modo de tela cheia
# No lugar do zoomed, coloca iconic e a janela inicia minimizada
menu_inicial.state("zoomed")

#Alterar o ícone da aplicação. digita o caminho onde o icon esta que é images, e dps o nome do icone.ico que é a extensao do icone
menu_inicial.iconbitmap("images/icon.ico")

#Alterar cor de fundo da janela
menu_inicial['bg'] = "blue"

#Criando botão
btn = Button(menu_inicial, text = "Executar")
btn.pack()







menu_inicial.mainloop()