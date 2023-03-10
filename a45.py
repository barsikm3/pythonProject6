import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

def search(*args):
    input = select_data.get()
    if len(input) < 2:
        return
    matching = [email for email in emails if input in email]
    select_data['values'] = matching

def show_options(*args):
    options_list.delete(0, tk.END)
    input = select_data.get()
    if len(input) < 2:
        return
    matching = [email for email in emails if input in email]
    for option in matching:
        options_list.insert(tk.END, option)

# Read data from excel file
df = pd.read_excel("file.xlsx")
emails = df["Email"].tolist()

root = tk.Tk()
root.title("Autocomplete Combo Box")

# Create combobox widget
select_data = ttk.Combobox(root, values=emails, state="normal")
select_data.pack()
select_data.bind("<KeyRelease>", search)
select_data.bind("<FocusIn>", lambda e: search())

# Create second button to show options
show_options_button = tk.Button(root, text="Show Options", command=show_options)
show_options_button.pack()

# Create listbox to display options
options_list = tk.Listbox(root, height=20)
options_list.pack()

root.mainloop()



