import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

def search(*args):
    input = select_data.get()
    if len(input) < 2:
        return
    matching = [email for email in emails if input in email]
    select_data['values'] = matching

# Read data from excel file
df = pd.read_excel("file.xlsx")
emails = df["Email"].tolist()

root = tk.Tk()
root.title("Autocomplete Combo Box")

# Create combobox widget
select_data = ttk.Combobox(root, values=emails, state="normal", height=20)
select_data.pack()
select_data.bind("<KeyRelease>", search)
select_data.bind("<FocusIn>", lambda e: search())

root.mainloop()


