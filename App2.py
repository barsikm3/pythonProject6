import tkinter as tk
import pandas as pd

def autocomplete(event):
    value = event.widget.get()
    list_options = [x for x in data['Column Name'] if x.startswith(value)]
    if list_options:
        popup_menu.listbox.delete(0, tk.END)
        for option in list_options:
            popup_menu.listbox.insert(tk.END, option)
        popup_menu.listbox.selection_clear(0, tk.END)
        popup_menu.listbox.activate(0)
        popup_menu.post(event.x_root, event.y_root)
    else:
        popup_menu.unpost()

def on_select(event):
    value = event.widget.get(event.widget.curselection())
    entry.delete(0, tk.END)
    entry.insert(0, value)
    popup_menu.unpost()

root = tk.Tk()
root.title("Autocomplete Combo Box")

# Read excel file
data = pd.read_excel("file.xlsx")

# Create entry widget
entry = tk.Entry(root)
entry.pack()
entry.bind("<KeyRelease>", autocomplete)

# Create listbox for options
popup_menu = tk.Menu(root, tearoff=0)
popup_menu.listbox = tk.Listbox(popup_menu, height=6, width=50)
popup_menu.listbox.pack(fill="both", expand=True)
popup_menu.listbox.bind("<Double-Button-1>", on_select)

root.mainloop()
