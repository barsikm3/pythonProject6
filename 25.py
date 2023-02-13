import tkinter as tk

root = tk.Tk()

text = tk.Text(root, height=10, width=50)
text.pack()

# Insert some text
text.insert(tk.END, "This is some text that can be redacted.")

# Create a custom tag called "redact"
text.tag_configure("redact", foreground="black", background="black")

def toggle_redact():
    # Get the current state of the "redact" tag
    current_state = text.tag_configure("redact")["background"]
    if current_state == "black":
        # If the tag is currently redacted, change it to be unredacted
        text.tag_configure("redact", foreground="black", background="white")
    else:
        # If the tag is currently unredacted, change it to be redacted
        text.tag_configure("redact", foreground="black", background="black")

button = tk.Button(root, text="Redact", command=toggle_redact)
button.pack()

root.mainloop()
