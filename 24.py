import tkinter as tk
import tkinter.filedialog
import tkinter.ttk as ttk
import pandas as pd

def load_file():
    file_path = tkinter.filedialog.askopenfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        df = pd.read_excel(file_path)
        sheet_names = df.keys()
        sheet_var.set(sheet_names[0])
        update_column_names(df[sheet_names[0]])

def update_column_names(df):
    column_names = list(df.columns)
    column_var.set(column_names[0])
    column_names_menu = column_names_dropdown["menu"]
    column_names_menu.delete(0, "end")
    for name in column_names:
        column_names_menu.add_command(label=name, command=lambda value=name: column_var.set(value))

def update_emails(df, column_name):
    global emails
    emails = df[column_name].tolist()

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

load_button = tk.Button(root, text="Load File", command=load_file)
load_button.pack(pady=10)

sheet_var = tk.StringVar()
sheet_dropdown = ttk.OptionMenu(root, sheet_var, [], command=lambda sheet: update_column_names(df[sheet]))
sheet_dropdown.pack(pady=10)

column_var = tk.StringVar()
column_names_dropdown = ttk.OptionMenu(root, column_var, [], command=lambda column: update_emails(df[sheet_var.get()], column))
column_names_dropdown.pack(pady=10)

select_data = ttk.Combobox(root, values=[], state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root, height=5)
results_list.pack(pady=10)
results_list.bind("<Button-1>", select_email)

root.mainloop()


