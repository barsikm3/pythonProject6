import tkinter as tk

root = tk.Tk()

# Create a font object to use in the Text widget
my_font = ("Arial", 12)

# Create a Text widget with the font object
text = tk.Text(root, height=10, width=50, font=my_font)
text.pack()

# Insert some text with a hyperlink
text.insert(tk.END, "This is some text with a ")
text.insert(tk.END, "hyperlink", ("hyperlink", "underline"))
text.insert(tk.END, ".\n")

# Define a function to handle clicking the hyperlink
def callback(event):
    text.tag_configure("hyperlink", foreground="blue")
    webbrowser.open_new(event.widget.get("current linestart", "current lineend"))

# Add a tag for the hyperlink and bind it to the callback function
text.tag_configure("hyperlink", foreground="blue", underline=1)
text.tag_bind("hyperlink", "<Button-1>", callback)

# Create a button to copy the text to the clipboard
def copy_text():
    root.clipboard_clear()
    root.clipboard_append(text.get("1.0", tk.END))

button_copy = tk.Button(root, text="Copy", command=copy_text)
button_copy.pack()

root.mainloop()

