import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from tkinter import filedialog

def search(*args):
    input = select_data.get()
    if len(input) < 2:
        results_list.delete(0, tk.END)
        return
    matching = [email for email in column_values if input in email]
    results_list.delete(0, tk.END)
    for email in matching:
        results_list.insert(tk.END, email)

def select_email(*args):
    selection = results_list.get(results_list.curselection())
    select_data.set(selection)

def load_file():
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)
    sheets = df.columns.tolist()
    sheet_dropdown['values'] = sheets
    sheet_dropdown.current(0)

def change_sheet(*args):
    sheet = sheet_dropdown.get()
    df = pd.read_excel(file_path, sheet_name=sheet)
    column_values = df.iloc[:,0].tolist()
    select_data['values'] = column_values

root = tk.Tk()
root.title("Autocomplete Search")

load_file_button = tk.Button(root, text="Load Excel File", command=load_file)
load_file_button.pack(pady=10)

sheet_dropdown = ttk.Combobox(root, state="readonly")
sheet_dropdown.bind("<<ComboboxSelected>>", change_sheet)
sheet_dropdown.pack(pady=10)

select_data = ttk.Combobox(root, state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root, height=5)
results_list.pack(pady=10)
results_list.bind("<Button-1>", select_email)

root.mainloop()

