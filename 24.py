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

def load_file():
    global emails
    file_path = fd.askopenfilename()
    if file_path:
        df = pd.read_excel(file_path, sheet_name=sheet_var.get())
        emails = df["Email"].tolist()
        select_data["values"] = emails

root = tk.Tk()
root.title("Autocomplete Search")

load_button = tk.Button(root, text="Load File", command=load_file)
load_button.pack(pady=10)

sheet_var = tk.StringVar(root)
sheet_var.set("Sheet1")
sheet_dropdown = tk.OptionMenu(root, sheet_var, *["Sheet1", "Sheet2", "Sheet3"])
sheet_dropdown.pack(pady=10)

select_data = ttk.Combobox(root, values=[], state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root, height=5)
results_list.pack(pady=10)
results_list.bind("<Button-1>", select_email)

root.mainloop()
