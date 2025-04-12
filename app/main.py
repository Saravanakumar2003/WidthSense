import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import logging

# Configure logging
logging.basicConfig(filename="app.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

def calculate_widths(file_path, output_file_path, progress_var):
    try:
        df = pd.read_excel(file_path)

        # Validate required columns
        if 'x' not in df.columns or 'y' not in df.columns:
            raise ValueError("Input file must contain 'x' and 'y' columns.")

        x = df['x'].values
        y = df['y'].values

        # Sort data for consistency
        sorted_indices = np.argsort(x)
        x = x[sorted_indices]
        y = y[sorted_indices]

        y_min = np.floor(min(y) * 10) / 10
        y_max = np.ceil(max(y) * 10) / 10
        y_levels = np.arange(y_min, y_max + 0.1, 0.1)

        results = []
        total_levels = len(y_levels)

        for idx, level in enumerate(y_levels):
            crossings = []
            for i in range(len(y) - 1):
                if (y[i] - level) * (y[i+1] - level) <= 0 and y[i] != y[i+1]:
                    x_interp = x[i] + (level - y[i]) * (x[i+1] - x[i]) / (y[i+1] - y[i])
                    crossings.append(x_interp)

            if len(crossings) >= 2:
                x1 = min(crossings)
                x2 = max(crossings)
                width = x2 - x1
            else:
                width = None

            results.append({"y_level": round(level, 1), "width": width})

            # Update progress bar
            progress_var.set((idx + 1) / total_levels * 100)
            root.update_idletasks()

        output_df = pd.DataFrame(results)
        output_df.to_excel(output_file_path, index=False)
        return True
    except Exception as e:
        logging.error(f"Error in calculate_widths: {e}")
        messagebox.showerror("Error", str(e))
        return False
    
def select_input_file():
    global input_file_path
    input_file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if input_file_path:
        input_label.config(text=f"Input File: {input_file_path}")

def select_output_folder():
    global output_file_path
    output_folder = filedialog.askdirectory()
    if output_folder:
        output_file_path = f"{output_folder}/output.xlsx" 
        output_label.config(text=f"Output Folder: {output_folder}")

def process_files():
    if not input_file_path or not output_file_path:
        messagebox.showerror("Error", "Please select both input file and output folder.")
        return

    status_label.config(text="Processing...")
    root.update_idletasks()
    success = calculate_widths(input_file_path, output_file_path, progress_var)  # Pass progress_var here
    if success:
        status_label.config(text=f"✅ Saved as '{output_file_path}'")
        messagebox.showinfo("Done", f"Output saved as {output_file_path}")
    else:
        status_label.config(text="❌ Error")

# GUI setup
root = tk.Tk()
root.title("Width Calculation Tool")
root.geometry("500x300")
root.resizable(False, False)

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 10))

# Input file selection
input_file_path = None
output_file_path = None

input_label = ttk.Label(root, text="Input File: Not selected", foreground="blue")
input_label.pack(pady=5)

input_button = ttk.Button(root, text="Select Input File", command=select_input_file)
input_button.pack(pady=5)

# Output file selection
output_label = ttk.Label(root, text="Output Folder: Not selected", foreground="blue")
output_label.pack(pady=5)

output_button = ttk.Button(root, text="Select Output Folder", command=select_output_folder)
output_button.pack(pady=5)

# Process button
process_button = ttk.Button(root, text="Process", command=process_files)
process_button.pack(pady=10)

# Progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(pady=10)
progress_bar.config(length=400)

# Status label
status_label = ttk.Label(root, text="", foreground="blue")
status_label.pack(pady=10)

root.mainloop()