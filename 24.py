import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from tkinter import filedialog

def search(*args):
    input = select_data.get()
    if len(input) < 2:
        results_list.delete(0, tk.END)
        return
    column = column_var.get()
    matching = [email for email in df[column].tolist() if input in email]
    results_list.delete(0, tk.END)
    for email in matching:
        results_list.insert(tk.END, email)

def select_email(*args):
    selection = results_list.get(results_list.curselection())
    select_data.set(selection)

def load_file():
    file_path = filedialog.askopenfilename()
    global df
    df = pd.read_excel(file_path)
    sheet_names = df.keys()
    sheet_dropdown.config(values=sheet_names)

def update_sheet(*args):
    sheet_name = sheet_var.get()
    global df
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    column_names = df.keys()
    column_dropdown.config(values=column_names)

root = tk.Tk()
root.title("Autocomplete Search")

file_button = tk.Button(root, text="Choose File",






