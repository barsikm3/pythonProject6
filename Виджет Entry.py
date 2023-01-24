import tkinter as tk

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')
def get_delete():
    name.delete(0, tk.END)

def submit():
    print(name.get())
    print(password.get())
    get_delete()
    password.delete(0, tk.END)
win = tk.Tk()
win.geometry(f'400x500+100+200')
win.title("Entry")

name = tk.Entry(win)
password = tk.Entry(win, show='*')
name.grid(row=0,column=1, stick='e')
password.grid(row=1,column=1, stick='e')
tk.Label(win,text='Name').grid(row=0, column=0, stick='w')
tk.Label(win,text='Password').grid(row=1, column=0, stick='w')
tk.Button(win, text='get', command=get_entry).grid(row=2, column=1)
tk.Button(win, text='delete', command=get_delete).grid(row=2, column=2)
tk.Button(win, text='submit', command=submit).grid(row=4, column=2, stick='e')
tk.Button(win, text='Insert ', command=lambda: name.insert(1, "Insert ")).grid(row=3, column=2)
win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()