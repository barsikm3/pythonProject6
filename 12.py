import tkinter as tk
import tkinter.filedialog as fd
import tkinter.ttk as ttk
import pandas as pd

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

def select_file():
    file_path = fd.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if not file_path:
        return
    df = pd.read_excel(file_path)
    sheets = df.columns.tolist()
    sheet_var.set(sheets[0])
    sheet_menu.children["menu"].delete(0, "end")
    for sheet in sheets:
        sheet_menu.children["menu"].add_command(label=sheet, command=lambda value=sheet: sheet_var.set(value))
    emails = df[sheet_var.get()].tolist()
    select_data["values"] = emails

root = tk.Tk()
root.title("Autocomplete Search")

select_data = ttk.Combobox(root, values=[], state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root, height=5)
results_list.pack(pady=10)
results_list.bind("<Button-1>", select_email)

file_button = tk.Button(root, text="Select Excel File", command=select_file)
file_button.pack(pady=10)

sheet_var = tk.StringVar()
sheet_menu = ttk.OptionMenu(root, sheet_var, [])
sheet_menu.pack(pady=10)

root.mainloop()

