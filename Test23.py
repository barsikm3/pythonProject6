import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*xlsx")])
    df = pd.read_excel(file_path, sheet_name=None)
    column_names = list(df.columns)
    column_var.set(column_names[0])
    column_options['values'] = column_names

def update_results(search_value):
    selected_column = column_var.get()
    results = df[df[selected_column].str.contains(search_value, case=False)].loc[:, selected_column].tolist()
    result_list.delete(0, tk.END)
    for result in results[:5]:
        result_list.insert(tk.END, result)

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

file_button = tk.Button(window, text="Select Excel File", command=select_file)
file_button.bind("<KeyRelease>", search)
file_button.pack(pady=10)

column_var = tk.StringVar()
column_options = ttk.Combobox(window, textvariable=column_var, state="readonly")
column_options.pack()

df = pd.read_excel('Book23.xlsx')
emails = df["Email"].tolist()

select_data = ttk.Combobox(window, values=emails, state='normal')
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

result_list = tk.Listbox(window, height=5)
result_list.pack(pady=10)
result_list.bind("<Button-1>", select_email)



window.mainloop()
