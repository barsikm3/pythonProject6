import tkinter as tk

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')
win = tk.Tk()
win.geometry(f'400x500+100+200')
win.title("Entry")

name = tk.Entry(win)
name.grid(row=0,column=1, stick='e')
tk.Label(win,text='Name').grid(row=0, column=0, stick='w')
tk.Button(win, text='get', command=get_entry).grid(row=2, column=1)

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()