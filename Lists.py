import tkinter as tk

def create_new_list():
    selected_value = combobox.get()
    new_list = [selected_value] * 5
    print(new_list)

root = tk.Tk()

combobox = tk.ttk.Combobox(root, values=[1, 2, 3, 4, 5])
combobox.pack()

create_new_list_button = tk.Button(root, text="Create New List", command=create_new_list)
create_new_list_button.pack()

root.mainloop()


