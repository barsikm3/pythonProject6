import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from tkinter import filedialog


def search(*args):
    input = select_data.get()
    if len(input) < 2:
        results_list.delete(0, tk.END)
        return
    matching = []
    results_list.delete(0, tk.END)
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            cell_value = df.iloc[i, j]
            if input in str(cell_value):
                matching.append((i, cell_value))
    for i, e in matching:
        results_list.insert(tk.END, f"{e}")



def select_email(*args):
    selection = results_list.curselection()
    if selection:
        selected_row = int(results_list.get(selection[0]).split(" ")[1]) - 1
        selected_data = df.iloc[selected_row].tolist()
        select_data.set(f"Row {selected_row + 1}: " + ", ".join([str(x) for x in selected_data]))
        select_data.set(selection)


def load_file(*args):
    global df
    file_path = filedialog.askopenfilename()
    df = pd.read_excel(file_path)



root = tk.Tk()
root.title("Autocomplete Search")

select_data = ttk.Combobox(root, state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root, height=10)
results_list.pack(pady=25)
results_list.bind("<Button-1>", select_email)

load_button = tk.Button(root, text="Load Excel File", command=load_file)
load_button.pack(pady=10)

root.mainloop()
