from tkinter import *

janela = Tk()
janela.geometry('300x200')

#Função criada para ver o valor do slide
def verValor():
    print(slide.get())

#Vai de 1 a 100, na direção horizontal, para deixar vertical é so tirar o orient, no intervalo de 0.5 em 0.5
slide = Scale(janela, from_=1, to=100, orient=HORIZONTAL, resolution=0.5)
slide.pack()

bt = Button(janela, text='Ver valor', command=verValor)
bt.pack()


janela.mainloop()


