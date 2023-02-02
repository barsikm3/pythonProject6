import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

def search(*args):
    input = select_data.get()
    if len(input) < 2:
        return
    matching = [email for email in emails if input in email]
    if matching:
        select_data['values'] = matching
        select_data.set(matching[0])
    else:
        select_data['values'] = emails

# Read data from excel file
df = pd.read_excel("file.xlsx")
emails = df["Email"].tolist()

root = tk.Tk()
root.title("Autocomplete Combo Box")

# Create combobox widget
select_data = ttk.Combobox(root, values=emails, state="normal")
select_data.pack()
select_data.bind("<KeyRelease>", search)

root.mainloop()

