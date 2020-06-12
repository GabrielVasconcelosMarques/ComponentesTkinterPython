from tkinter import *

root = Tk()
root.geometry('500x500')

#Pegando o valor do textbox
def getvalor():
    result = text.get(1.0, END)
    print(result)

text = Text(root, width=20, height=10, wrap=WORD, padx=10, pady=10, bd=5)
text.pack()

bt1 = Button(root, text="Get valor", command=getvalor)
bt1.pack()

root.mainloop()