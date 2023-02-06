import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from tkinter import filedialog

def search(*args):
    input = select_data.get()
    if len(input) < 2:
        results_list.delete(0, tk.END)
        return
    matching = [email for email in emails if input in email]
    results_list.delete(0, tk.END)
    for email in matching:
        results_list.insert(tk.END, email)

def select_email(*args):
    selection = results_list.curselection()
    if selection:
        selection = results_list.get(selection[0])
        select_data.set(selection)

def load_file():
    global df, emails
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)
    sheets = df.sheet_names
    sheet_var.set(sheets[0])
    emails = df[sheet_var.get()]["Email"].tolist()
    select_data['values'] = emails

def change_sheet(*args):
    global emails
    emails = df[sheet_var.get()]["Email"].tolist()
    select_data['values'] = emails
    select_data.set("")
    results_list.delete(0, tk.END)

root = tk.Tk()
root.title("Autocomplete Search")

file_button = tk.Button(root, text="Select File", command=load_file)
file_button.pack(pady=10)

sheet_var = tk.StringVar(value="")
sheet_var.trace("w", change_sheet)
sheet_menu = tk.OptionMenu(root, sheet_var, [])
sheet_menu.pack(pady=10)

select_data = ttk.Combobox(root, values=[], state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root, height=5)
results_list.pack(pady=10)
results_list.bind("<Button-1>", select_email)

root.mainloop()
