root = tk.Tk()
root.title("Autocomplete Search")

select_data = ttk.Combobox(root, state="normal")
select_data.bind("<KeyRelease>", search)
select_data.pack(pady=10)

email_label = ttk.Label(root, text="Email:")
email_label.pack()
email = ttk.Entry(root, show="*")
email.pack()

password_label = ttk.Label(root, text="Password:")
password_label.pack()
password = ttk.Entry(root, show="*")
password.pack()

results_list = tk.Listbox(root, height=10)
results_list.pack(pady=25)
results_list.bind("<Button-1>", select_email)

load_button = tk.Button(root, text="Load Excel File", command=load_file)
load_button.pack(pady=10)

attach_button = tk.Button(root, text="Select Attachments", command=lambda: select_attachments(root))
attach_button.pack(pady=10)

send_button = tk.Button(root, text="Send Email", command=lambda: send_email(root, email, password))
send_button.pack(pady=10)

root.mainloop()

