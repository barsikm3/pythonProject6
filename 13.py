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
    selection = results_list.get(results_list.curselection())
    select_data.set(selection)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    df = pd.read_excel(file_path, sheet_name=None)
    sheet_names = list(df.keys())
    sheet_var.set(sheet_names[0])
    update_data(df, sheet_names[0])

def update_data(df, sheet_name):
    global emails
    emails = df[sheet_name]["Email"].tolist()
    select_data["values"] = emails

root = tk.Tk()
root.title("Autocomplete Search")

file_button = tk.Button(root, text="Select Excel File", command=select_file)
file_button.pack(pady=10)

sheet_var = tk.StringVar(value="")
sheet_label = tk.Label(root, textvariable=sheet_var)
sheet_label.pack(pady=10)

select_data = ttk.Combobox(root, values=[], state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)


results_list = tk.Listbox(root, height=5)
results_list.pack(pady=10)
results_list.bind("<Button-1>", select_email)

root.mainloop()
