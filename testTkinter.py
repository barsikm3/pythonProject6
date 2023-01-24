import tkinter as tk
win = tk.Tk()
win.geometry(f'300x400+100+210')
win.title("Урок номер 4")
win.config(bg="white")
#for i in range(7):
   # for j in range(4):
# tk.Button(win, text=f'Hey u bey latamarey {i} {j}').grid(row=i, column=j, stick='we')   метод по вкладке пачки кнопок
btn1 = tk.Button(win, text= "Hi there")
btn2 = tk.Button(win, text= "Hi there one more time")
btn3 = tk.Button(win, text= "Argentina")
btn4 = tk.Button(win, text= "is")
btn5 = tk.Button(win, text= "the")
btn6 = tk.Button(win, text= "best")
btn7 = tk.Button(win, text= "team")
btn8 = tk.Button(win, text= "in the world")
btn9 = tk.Button(win, text= "and that is the third time winner")

btn1.grid(row=0, column=0, stick='w')
btn2.grid(row=1, column=0, stick='w')
btn3.grid(row=2, column=0, stick='w')
btn4.grid(row=3, column=0, stick='we')
btn5.grid(row=0, column=2)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=2)
btn8.grid(row=3, column=2, columnspan=2, stick='w')
btn9.grid(row=4, column=0, columnspan=2, stick='w')



win.grid_columnconfigure(0,minsize=200)

win.mainloop()