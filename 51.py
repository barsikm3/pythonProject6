import tkinter as tk
import pandas as pd
from tkinter import filedialog
from tkinter import ttk

root = tk.Tk()
root.geometry("400x400")

def import_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        df = pd.read_excel(file_path)
        column_names = list(df.columns)
        column_var.set(column_names[0])
        columns_menu = tk.OptionMenu(root, column_var, *column_names)
        columns_menu.pack()

def update_combo_values(value):
    select_data["values"] = df[column_var.get()].tolist()

def search(event=None):
    input_value = select_data.get()
    similar_values = [value for value in select_data["values"] if input_value in value]
    search_results.config(text="\n".join(similar_values[:5]))

column_var = tk.StringVar()
import_button = tk.Button(root, text="Import Excel", command=import_excel)
import_button.pack()
select_data = ttk.Combobox(root, values=[], state="readonly")
select_data.bind("<<ComboboxSelected>>", lambda event: update_combo_values(event))
select_data.pack()
search_results = tk.Label(root, text="", wraplength=250)
search_results.pack()
select_data.bind("<KeyRelease>", search)

root.mainloop()
