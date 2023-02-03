import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import tkinter.filedialog as fd

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

def open_file():
    file_path = fd.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        df = pd.read_excel(file_path)
        sheet_names = df.sheet_names
        sheet_name = tk. simpledialog.askstring("Sheet Name", "Enter the sheet name", initialvalue=sheet_names[0])
        if sheet_name:
            emails = df[sheet_name]["Email"].tolist()
            select_data["values"] = emails

root = tk.Tk()
root.title("Autocomplete Search")

open_file_button = tk.Button(root, text="Open Excel File", command=open_file)
open_file_button.pack(pady=10)

select_data = ttk.Combobox(root, values=[], state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root, height=5)
results_list.pack(pady=10)
results_list.bind("<Button-1>", select_email)

root.mainloop()
