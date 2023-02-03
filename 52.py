import tkinter as tk
import tkinter.filedialog
import pandas as pd
from tkinter import ttk

def select_file():
    file_path = tk.filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        df = pd.read_excel(file_path)
        column_names = list(df.columns)
        column_var.set(column_names[0])
        column_options['values'] = column_names

def update_results(search_value):
    selected_column = column_var.get()
    results = df[df[selected_column].str.contains(search_value, case=False)].loc[:, selected_column].tolist()
    results_list.delete(0, tk.END)
    for result in results[:5]:
        results_list.insert(tk.END, result)

def on_result_click(event):
    result = results_list.get(results_list.curselection()[0])
    combo.set(result)
    results_list.pack_forget()

root = tk.Tk()
root.title("Excel Autocomplete Search")

file_select_button = tk.Button(root, text="Select Excel File", command=select_file)
file_select_button.pack()

column_var = tk.StringVar()
column_options = ttk.Combobox(root, textvariable=column_var, state="readonly")
column_options.pack()

combo = ttk.Combobox(root, values=[], height=5)
combo.pack()

results_list = tk.Listbox(root, height=5)
results_list.pack_forget()
results_list.bind("<<ListboxSelect>>", on_result_click)

combo.bind("<<ComboboxSelected>>", lambda event: results_list.pack_forget())
combo.bind("<KeyRelease>", lambda event: update_results(combo.get()))

root.mainloop()
