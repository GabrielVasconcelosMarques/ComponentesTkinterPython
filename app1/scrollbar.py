from tkinter import *

root = Tk()
root.geometry("500x500")

frame = Frame(root, relief="solid", borderwidth=2, bg="lightblue")
frame.pack(fill=BOTH)

scroll1 = Scrollbar(frame, orient=HORIZONTAL)
scroll1.pack(side=BOTTOM, fill=X)

scroll2 = Scrollbar(frame, orient=VERTICAL)
scroll2.pack(side=RIGHT, fill=Y)

#Codigo que pega bem o scrollbar
'''from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()'''

root.mainloop()