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
label_1.pack()
tk.mainloop()
