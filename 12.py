import tkinter as tk
import tkinter.filedialog as fd
import tkinter.ttk as ttk
import pandas as pd

def select_file():
    file_path = fd.askopenfilename()
    if not file_path:
        return
    df = pd.read_excel(file_path)
    sheet_names = df.sheet_names
    selected_sheet = tk.StringVar()
    selected_column = tk.StringVar()
    sheet_selector = ttk.OptionMenu(root, selected_sheet, *sheet_names)
    sheet_selector.pack()
    column_selector = ttk.OptionMenu(root, selected_column, *df[selected_sheet.get()].columns)
    column_selector.pack()

    def change_column(*args):
        column_selector['menu'].delete(0, 'end')
        new_columns = df[selected_sheet.get()].columns
        new_column_var = tk.StringVar()
        for column in new_columns:
            column_selector['menu'].add_command(label=column, command=lambda value=column: new_column_var.set(value))
        selected_column.set(new_columns[0])

    selected_sheet.trace('w', change_column)

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

root = tk.Tk()
root.title("Autocomplete Search")

select_file_button = ttk.Button(root, text="Select Excel file", command=select_file)
select_file_button.pack(pady=10)

select_data = ttk.Combobox(root, values=[], state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root, height=5)
results_list.pack(pady=10)
results_list.bind("<Button-1>", select_email)

root.mainloop()
