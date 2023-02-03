import tkinter as tk
from tkinter import ttk
import pandas as pd

def search_data():
    search_term = combo.get()
    results = []
    for item in df[column_name].tolist():
        if search_term in item:
            results.append(item)
    results_box.config(state=tk.NORMAL)
    results_box.delete(0, tk.END)
    for result in results:
        results_box.insert(tk.END, result)
    results_box.config(state=tk.DISABLED)

def select_data(event):
    selected = results_box.get(results_box.curselection())
    combo.set(selected)
    results_box.config(state=tk.NORMAL)
    results_box.delete(0, tk.END)
    results_box.config(state=tk.DISABLED)

def choose_file():
    global df
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)
    columns = df.columns
    column_var.set(columns[0])
    column_menu = tk.OptionMenu(root, column_var, *columns)
    column_menu.grid(row=0, column=1)

root = tk.Tk()
root.title("Excel Autocomplete")

column_var = tk.StringVar()

file_button = tk.Button(root, text="Choose Excel File", command=choose_file)
file_button.grid(row=0, column=0)

combo = ttk.Combobox(root, values=[], height=5)
combo.grid(row=1, column=0, columnspan=2)
combo.bind("<KeyRelease>", search_data)

results_box = tk.Listbox(root, height=5, state=tk.DISABLED)
results_box.grid(row=2, column=0, columnspan=2)
results_box.bind("<Double-Button-1>", select_data)

root.mainloop()
