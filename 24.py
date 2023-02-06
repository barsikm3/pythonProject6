import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from tkinter import filedialog

def load_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    global df
    df = pd.read_excel(file_path, sheet_name=None)
    sheet_names = list(df.keys())
    sheet_var.set(sheet_names[0])
    sheet_selector['values'] = sheet_names

def change_sheet(*args):
    sheet_name = sheet_var.get()
    global emails
    emails = df[sheet_name]['Email'].tolist()
    select_data['values'] = emails

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
    selection = results_list.get(results_list.curselection())
    select_data.set(selection)

root = tk.Tk()
root.title("Autocomplete Search")

load_file_button = tk.Button(root, text="Load Excel File", command=load_file)
load_file_button.pack(pady=10)

sheet_var = tk.StringVar()
sheet_selector = ttk.Combobox(root, textvariable=sheet_var, state="readonly")
sheet_selector.bind("<<ComboboxSelected>>", change_sheet)
sheet_selector.pack(pady=10)

select_data = ttk.Combobox(root, state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root, height=5)
results_list.pack(pady=10)
results_list.bind("<Button-1>", select_email)

root.mainloop()
