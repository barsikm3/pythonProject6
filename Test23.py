import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

def search(*args):
    input = select_data.get()
    if len(input) < 2:
        result_list.delete(0, tk.END)
        return
    matching = [email for email in emails if input in email]
    result_list.delete(0, tk.END)
    for email in matching:
        result_list.insert(tk.END, email)



def select_email(*args):
    selection = result_list.curselection()
    if selection:
        selection = result_list.get(selection[0])
        select_data.set(selection)


window = tk.Tk()
window.title = ('Corporate automate selection')

df = pd.read_excel('Book23.xlsx')
emails = df["Email"].tolist()

select_data = ttk.Combobox(window, values=emails, state='normal')
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

result_list = tk.Listbox(window, height=5)
result_list.pack(pady=10)
result_list.bind("<Button-1>", select_email)



window.mainloop()
