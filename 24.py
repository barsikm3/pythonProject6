import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import os
from tkinter import filedialog

def load_file():
    global df, emails
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)
    column_names = df.columns
    if 'Email' in column_names:
        emails = df['Email'].tolist()
    else:
        tk.messagebox.showerror("Error", "Email column not found in the excel file.")

def search(*args):
    input = select_data.get()
    if len(input) < 2:
        results_list.delete(0, tk.END)
        return
    if 'emails' in globals():
        matching = [email for email in emails if input in email]
        results_list.delete(0, tk.END)
        for email in matching:
            results_list.insert(tk.END, email)
    else:
        tk.messagebox.showerror("Error", "Please load an excel file with Email column.")

def select_email(*args):
    selection = results_list.get(results_list.curselection())
    select_data.set(selection)

root = tk.Tk()
root.title("Autocomplete Search")

load_file_btn = tk.Button(root, text="Load Excel File", command=load_file)
load_file_btn.pack(pady=10)

select_data = ttk.Combobox(root, state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root, height=5)
results_list.pack(pady=10)
results_list.bind("<Button-1>", select_email)

root.mainloop()

