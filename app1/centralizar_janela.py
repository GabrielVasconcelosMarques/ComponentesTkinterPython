from tkinter import *





janela = Tk()
janela.title("Titulo")

#Dimensoes da janela
largura = 500
altura = 300

#Resolução do nosso sistema
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()


#Posição da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

#Definir a geometry
#janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
janela.geometry("500x300+%d+%d" % (posx, posy))

janela.mainloop()