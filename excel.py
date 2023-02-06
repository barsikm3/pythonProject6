from tkinter import *
root = Tk()

var = IntVar()
var.set(0)
c = Checkbutton(root, text="Hi all", variable=var)
c.pack()
root.mainloop()
