import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from tkinter import filedialog

def search(*args):
    input = select_data.get()
    if len(input) < 2:
        results_list.delete(0, tk.END)
        return
    matching = [email for email in df[selected_column] if input in email]
    results_list.delete(0, tk.END)
    for email in matching:
        results_list.insert(tk.END, email)

def select_email(*args):
    selection = results_list.get(results_list.curselection())
    select_data.set(selection)
    
def load_file(*args):
    global df, selected_column
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)
    columns = df.columns.tolist()
    column_dropdown.config(values=columns)
    selected_column = columns[0]

root = tk.Tk()
root.title("Autocomplete Search")

select_data = ttk.Combobox(root, state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root, height=5)
results_list.pack(pady=10)
results_list.bind("<Button-1>", select_email)

load_button = tk.Button(root, text="Load Excel File", command=load_file)
load_button.pack(pady=10)

column_dropdown = ttk.Combobox(root, state="disabled")
column_dropdown.pack(pady=10)
column_dropdown.bind("<<ComboboxSelected>>", lambda e: setattr(df, "selected_column", column_dropdown.get()))

root.mainloop()





