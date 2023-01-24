def currency():
    print(f'The cost in is')
def add_label():
    print("That is a new label")
count = 0
def counter():
    global count
    count+=1
    btn4['text'] = f'Counter: {count}'




import tkinter as tk
win = tk.Tk()
win.title('Графическое окно')
h = 300
w = 450
win.geometry(f'{h}x{w}+20+20')
win.resizable(True, True)
photo = tk.PhotoImage(file="icons8-picture-100.png")
win.config(bg="#620BB9")
win.iconphoto(False, photo)
win.minsize(200,300)
win.maxsize(1000,1200)
#лейблы и все что с этим связано
label_1 = tk.Label(win, text="""That is a 
first method""",  #многострочный метод """
                   bg="black",
                   fg="violet",
                   font=("Arial",20,"bold"),
                   padx=30,
                   pady=40,
                   height=10,
                   width=20,
                   anchor="w",
                   relief=tk.RAISED, #огранка, фон кнопки
                   bd=20, #ширина самого фона
                   justify=tk.RIGHT # привязка
                   )
btn1 = tk.Button(win, text='Argentina the world cup champione',
                 command=currency                    #здесь мы указываем функцию и как мы можем ее использовать, фукция пишется
                 # пишется над TK
                 )
btn2 = tk.Button(win, text='Argentina the best team',
                 command=add_label                    #здесь мы указываем функцию и как мы можем ее использовать, фукция пишется
                 # пишется над TK
                 )
btn3 = tk.Button(win, text='spain maybe win the next EURo',
                 command=lambda: tk.Label(win, text="This is lambda").pack()                    #здесь мы указываем функцию и как мы можем ее использовать, фукция пишется
                 # пишется над TK
                 )
btn4 = tk.Button(win, text=f'Counter: {count}',
                 command=counter,
                 activebackground="blue",
                 bg="violet",
                 state=tk.NORMAL
                 )

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
label_1.pack()
tk.mainloop()
