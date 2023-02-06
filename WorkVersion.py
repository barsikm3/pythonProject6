import tkinter as tk
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
    selection = results_list.curselection()
    if selection:
        selection = results_list.get(selection[0])
        select_data.set(selection)

root = tk.Tk()
root.title("Autocomplete Search")

df = pd.read_excel("Book23.xlsx")
emails = df["Email"].tolist()

select_data = ttk.Combobox(root, values=emails, state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

results_list = tk.Listbox(root, height=5)
results_list.pack(pady=10)
results_list.bind("<Button-1>", select_email)

root.mainloop()
