import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

def hash_file(fileName):
    """Compute the SHA-1 hash of a file."""
    h = hashlib.sha1()
    try:
        with open(fileName, "rb") as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)  # Read file in chunks of 1024 bytes
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file: {e}")
        return None

def compare_files():
    """Compare two files using their SHA-1 hash values."""
    if not file1_path.get() or not file2_path.get():
        messagebox.showwarning("Warning", "Please upload both files.")
        return

    hash1 = hash_file(file1_path.get())
    hash2 = hash_file(file2_path.get())

    if hash1 and hash2:
        if hash1 == hash2:
            messagebox.showinfo("Result", "These files are identical.")
        else:
            messagebox.showinfo("Result", "These files are not identical.")

def browse_file1():
    """Open file dialog to select the first file."""
    filepath = filedialog.askopenfilename()
    if filepath:
        file1_path.set(filepath)

def browse_file2():
    """Open file dialog to select the second file."""
    filepath = filedialog.askopenfilename()
    if filepath:
        file2_path.set(filepath)

root = tk.Tk()
root.title("File Comparator")
root.geometry("500x300")

file1_path = tk.StringVar()
file2_path = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True)

tk.Label(frame, text="File 1:").grid(row=0, column=0, sticky="e")
file1_entry = tk.Entry(frame, textvariable=file1_path, width=40)
file1_entry.grid(row=0, column=1, padx=5)
browse1_button = tk.Button(frame, text="Browse", command=browse_file1)
browse1_button.grid(row=0, column=2, padx=5)

tk.Label(frame, text="File 2:").grid(row=1, column=0, sticky="e")
file2_entry = tk.Entry(frame, textvariable=file2_path, width=40)
file2_entry.grid(row=1, column=1, padx=5)
browse2_button = tk.Button(frame, text="Browse", command=browse_file2)
browse2_button.grid(row=1, column=2, padx=5)

compare_button = tk.Button(frame, text="Compare Files", command=compare_files, bg="green", fg="white")
compare_button.grid(row=2, column=0, columnspan=3, pady=20)

# Run the application
root.mainloop()
