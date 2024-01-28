import tkinter as tk
import pyperclip


def generate_macro():
    # Get input from user
    job = job_entry.get()
    gs = gs_entry.get()

    # Generate macro string
    macro = f"/gs change {gs}\r\n/micon \"Soul of the {job}\" item"

    # Copy macro to clipboard
    pyperclip.copy(macro)

    # Update status message
    status_label.config(text="Macro copied to clipboard")


# Create main window
root = tk.Tk()
root.title("Macro Generator")

# Create input labels and entries
job_label = tk.Label(root, text="Class:")
job_entry = tk.Entry(root)

gs_label = tk.Label(root, text="Gear Set #:")
gs_entry = tk.Entry(root)

# Create generate button
generate_button = tk.Button(root, text="Generate", command=generate_macro)

# Create status label
status_label = tk.Label(root, text="")

# Arrange widgets in grid
job_label.grid(row=0, column=0)
job_entry.grid(row=0, column=1)

gs_label.grid(row=1, column=0)
gs_entry.grid(row=1, column=1)

generate_button.grid(row=2, column=0, columnspan=2)

status_label.grid(row=3, column=0, columnspan=2)

# Start main loop
root.mainloop()

