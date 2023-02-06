import tkinter as tk
import tkinter.filedialog as fd
import pandas as pd
from tkinter import ttk

def load_file():
    file_path = fd.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if not file_path:
        return
    df = pd.read_excel(file_path)
    columns = df.columns
    sheet_dropdown.config(values=columns)

def select_sheet(*args):
    column = sheet_dropdown.get()
    select_data.config(values=df[column].tolist())

def search(*args):
    input = select_data.get()
    if len(input) < 2:
        results_list.delete(0, tk.END)
        return
    matching = [email for email in df[sheet_dropdown.get()] if input in str(email)]
    results_list.delete(0, tk.END)
    for email in matching:
        results_list.insert(tk.END, email)

def select_email(*args):
    selection = results_list.get(results_list.curselection())
    select_data.set(selection)

root = tk.Tk()
root.title("Autocomplete Search")

load_file_btn = tk.Button(root, text="Load File", command=load_file)
load_file_btn.pack(pady=10)

sheet_dropdown = ttk.Combobox(root, state="readonly")
sheet_dropdown.bind("<<ComboboxSelected>>", select_sheet)
sheet_dropdown.pack(pady=10)

select_data = ttk.Combobox(root, state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root, height=5)
results_list.pack(pady=10)
results_list.bind("<Button-1>", select_email)

root.mainloop()




