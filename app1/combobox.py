from tkinter import *
from tkinter.ttk import Combobox


root = Tk()
root.geometry("500x500")

#Valores que terão no combobox, para importar deve seguir a biblioteca acima
v=['1', '2', '3', '4', '5']

combo = Combobox(root, values=v)
combo.set("select")
combo.pack()

#Função para pegar valor do combobox
def pegarvalor():
    value = combo.get()
    print(value)

bt1 = Button(root, text="Pegar valor", command=pegarvalor)
bt1.pack()

root.mainloop()