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

def load_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    df = pd.read_excel(file_path)
    sheets = df.sheet_names
    sheet = tk.StringVar()
    sheet.set(sheets[0])
    
    def select_sheet(*args):
        nonlocal df, sheet_dropdown, select_data, results_list
        selected_sheet = sheet.get()
        df = pd.read_excel(file_path, sheet_name=selected_sheet)
        columns = df.columns
        column = tk.StringVar()
        column.set(columns[0])
        
        def select_column(*args):
            nonlocal df, column_dropdown, select_data, results_list
            selected_column = column.get()
            emails = df[selected_column].tolist()
            select_data.configure(values=emails)
        
        column_dropdown = ttk.OptionMenu(root, column, *columns, command=select_column)
        column_dropdown.pack()

    sheet_dropdown = ttk.OptionMenu(root, sheet, *sheets, command=select_sheet)
    sheet_dropdown.pack()

root = tk.Tk()
root.title("Autocomplete Search")

load_file_button = tk.Button(root, text="Load Excel File", command=load_file)
load_file_button.pack(pady=10)

select_data = ttk.Combobox(root, state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root, height=5)
results_list.pack(pady=10)
results_list.bind("<Button-1>", select_email)

root.mainloop()


