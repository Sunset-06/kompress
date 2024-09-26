import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import requests

def compress_file(file_path, output_path):
    try:
        data = {
            'filePath': file_path,
            'outputPath': output_path
        }
        response = requests.post('http://localhost:8080/api/compress', data=data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "File compressed successfully!")
        else:
            messagebox.showerror("Error", "Failed to compress file.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decompress_file(file_path, output_dir):
    try:
        data = {
            'filePath': file_path,
            'outputDir': output_dir
        }
        response = requests.post('http://localhost:8080/api/decompress', data=data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "File decompressed successfully!")
        else:
            messagebox.showerror("Error", "Failed to decompress file.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file(entry, file_types):
    file_path = filedialog.askopenfilename(title="Select File", filetypes=file_types)
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def browse_output_file(entry):
    output_path = filedialog.asksaveasfilename(title="Select Output Location", defaultextension=".7z", filetypes=[("7z files", "*.7z")])
    entry.delete(0, tk.END)
    entry.insert(0, output_path)

def browse_output_dir(entry):
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    entry.delete(0, tk.END)
    entry.insert(0, output_dir)

def switch_section(selection, compress_frame, decompress_frame):
    if selection == "Compress":
        compress_frame.grid(row=1, column=0, sticky="nsew")
        decompress_frame.grid_forget()
    else:
        compress_frame.grid_forget()
        decompress_frame.grid(row=1, column=0, sticky="nsew")

def create_gui():
    root = tk.Tk()
    style = ttk.Style(root) 

    root.tk.call('source', 'forest-dark.tcl')
    style.theme_use('forest-dark')
    root.option_add('*foreground', 'black')

    root.title("Kompress")
    root.geometry("1400x900")  

    frame = ttk.Frame(root, padding="30")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    options = ["Compress", "Decompress"]
    selected_option = tk.StringVar(value=options[0])
    dropdown = ttk.Combobox(frame, values=options, textvariable=selected_option, state="readonly")
    dropdown.grid(row=0, column=0, pady=10, padx=10)

    compress_frame = ttk.LabelFrame(frame, text="Compress", padding="10")
    decompress_frame = ttk.LabelFrame(frame, text="Decompress", padding="10")

    # Compress Section
    ttk.Label(compress_frame, text="File to Compress:").grid(row=0, column=0, pady=5, sticky=tk.E)
    compress_file_path = ttk.Entry(compress_frame, width=50)
    compress_file_path.grid(row=0, column=1, pady=5)
    browse_compress_file_button = ttk.Button(compress_frame, text="Browse", command=lambda: browse_file(compress_file_path, [("All Files", "*.*")]))
    browse_compress_file_button.grid(row=0, column=2, pady=5)

    ttk.Label(compress_frame, text="Output Path:").grid(row=1, column=0, pady=5, sticky=tk.E)
    compress_output_path = ttk.Entry(compress_frame, width=50)
    compress_output_path.grid(row=1, column=1, pady=5)
    browse_compress_output_button = ttk.Button(compress_frame, text="Browse", command=lambda: browse_output_file(compress_output_path))
    browse_compress_output_button.grid(row=1, column=2, pady=5)

    compress_button = ttk.Button(compress_frame, text="Compress", command=lambda: compress_file(compress_file_path.get(), compress_output_path.get()))
    compress_button.grid(row=2, column=0, columnspan=3, pady=10)

    # Decompress Section
    ttk.Label(decompress_frame, text="File to Decompress:").grid(row=0, column=0, pady=5, sticky=tk.E)
    decompress_file_path = ttk.Entry(decompress_frame, width=50)
    decompress_file_path.grid(row=0, column=1, pady=5)
    browse_decompress_file_button = ttk.Button(decompress_frame, text="Browse", command=lambda: browse_file(decompress_file_path, [("7z files", "*.7z")]))
    browse_decompress_file_button.grid(row=0, column=2, pady=5)

    ttk.Label(decompress_frame, text="Output Directory:").grid(row=1, column=0, pady=5, sticky=tk.E)
    decompress_output_dir = ttk.Entry(decompress_frame, width=50)
    decompress_output_dir.grid(row=1, column=1, pady=5)
    browse_decompress_output_button = ttk.Button(decompress_frame, text="Browse", command=lambda: browse_output_dir(decompress_output_dir))
    browse_decompress_output_button.grid(row=1, column=2, pady=5)

    decompress_button = ttk.Button(decompress_frame, text="Decompress", command=lambda: decompress_file(decompress_file_path.get(), decompress_output_dir.get()))
    decompress_button.grid(row=2, column=0, columnspan=3, pady=10)

    dropdown.bind("<<ComboboxSelected>>", lambda e: switch_section(selected_option.get(), compress_frame, decompress_frame))
    
    compress_frame.grid(row=1, column=0, sticky="nsew")
    
    # Configure grid weights
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
