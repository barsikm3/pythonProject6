import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import filedialog

def select_column():
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)
    columns = list(df.columns)
    column_var.set(columns[0])
    column_dropdown['values'] = columns

def update_list(*args):
    search = combobox.get().lower()
    filtered_list = [email for email in df[column_var.get()].tolist() if search in email.lower()]
    listbox.delete(0, tk.END)
    for email in filtered_list[:5]:
        listbox.insert(tk.END, email)

root = tk.Tk()
root.geometry("400x400")

column_var = tk.StringVar()

select_file_button = tk.Button(root, text="Select Excel File", command=select_column)
select_file_button.pack()

column_dropdown = ttk.Combobox(root, textvariable=column_var, state="readonly")
column_dropdown.pack()

combobox = ttk.Combobox(root, values=[], height=5, state="normal")
combobox.pack()
combobox.bind("<KeyRelease>", update_list)

listbox = tk.Listbox(root, height=5)
listbox.pack()

root.mainloop()
