from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Teste de messagebox")
root.geometry("500x500")

def showinfo():
    messagebox.showinfo("OK", "Aplication is sucessfull")

def showerror():
    messagebox.showerror("ERROR", "Aplication is not sucessfull")

def showwarning():
    messagebox.showwarning("WARNING", "Warning in aplication")

def exit():
    answer = messagebox.askquestion("EXIT", "Do you really want to exit?")
    if answer == "yes":
        root.quit()

def yesnocancel():
    answer = messagebox.askyesnocancel("Exit", "Do you really want to exit? ")
    if answer:
        root.quit()

def askokcancel():
    messagebox.askokcancel("OKExit", "Ok or Cancel?")

def repetir():
    messagebox.askretrycancel("ok", "Você deseja repetir? ")

def simnao():
    messagebox.askyesno("ok", "yesno")


bt1 = Button(root, text="Messagebox showinfo", command=showinfo)
bt1.pack()

bt2 = Button(root, text="Messagebox showerror", command=showerror)
bt2.pack()

bt3 = Button(root, text="Messagebox showwarning", command=showwarning)
bt3.pack()

bt4 = Button(root, text="Exit", command=exit)
bt4.pack()

bt5 = Button(root, text="Exit 2", command=yesnocancel)
bt5.pack()

bt6 = Button(root, text="Exit 3", command=askokcancel)
bt6.pack()

bt7 = Button(root, text="Repetir", command=repetir)
bt7.pack()

bt8 = Button(root, text="SIM ou NAO", command=simnao)
bt8.pack()




root.mainloop()