import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

def search(*args):
    input = select_data.get()
    if len(input) < 2:
        results_data['values'] = []
        return
    matching = [email for email in emails if input in email]
    results_data['values'] = matching
    results_data.current(0)

# Read data from excel file
df = pd.read_excel("file.xlsx")
emails = df["Email"].tolist()

root = tk.Tk()
root.title("Autocomplete Combo Box")

# Create first combobox widget
select_data = ttk.Combobox(root, values=emails, state="normal")
select_data.pack()
select_data.bind("<KeyRelease>", search)
select_data.bind("<FocusIn>", lambda e: search())

# Create second combobox widget
results_data = ttk.Combobox(root, state="readonly")
results_data.pack()
results_data.bind("<<ComboboxSelected>>", lambda e: select_data.set(results_data.get()))

root.mainloop()
