from tkinter import *
menu_inicial = Tk()
menu_inicial.geometry("400x400")

#Posicionamento grid, você declara numero de linha e depois coluna
lbl1 = Label(menu_inicial, text="Label 1", font="arial 20", bg="red")
lbl1.grid(row=0, column=0)

lbl2 = Label(menu_inicial, text="Label 2", font="arial 20", bg="yellow")
lbl2.grid(row=0, column=1)


menu_inicial.mainloop()