import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from tkinter import filedialog


def search(*args):
    input = select_data.get()
    if len(input) < 2:
        return
    matching = []
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            cell_value = df.iloc[i, j]
            if input in str(cell_value):
                matching.append((i, cell_value))
    results_list.delete(0, tk.END)
    for i, e in matching:
        results_list.insert(tk.END, f"{e}")


def select_email(*args):
    selection = results_list.curselection()
    if selection:
        selected_row = int(results_list.get(selection[0]).split(" ")[1]) - 1
        selected_data = df.iloc[selected_row].tolist()
        select_data.set(f"Row {selected_row + 1}: " + ", ".join([str(x) for x in selected_data]))


def load_file(*args):
    global df
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)
    results_list["height"] = min(10, df.shape[0])


root = tk.Tk()
root.title("Autocomplete Search")

select_data = ttk.Combobox(root, state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root)
