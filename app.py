import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Pilih file CSV", filetypes=[("CSV Files", "*.csv")])
    if file_path:
        file_label.config(text=f"File dipilih: {file_path}")
    else:
        file_label.config(text="Tidak ada file yang dipilih.")

def select_output_folder():
    global export_dir
    export_dir = filedialog.askdirectory(title="Pilih folder untuk menyimpan file hasil")
    if export_dir:
        folder_label.config(text=f"Folder dipilih: {export_dir}")
    else:
        folder_label.config(text="Tidak ada folder yang dipilih.")

def split_file():
    try:
        # Validasi input
        if not file_path:
            messagebox.showerror("Error", "Silakan pilih file CSV terlebih dahulu.")
            return
        if not export_dir:
            messagebox.showerror("Error", "Silakan pilih folder untuk menyimpan file.")
            return

        # Meminta nama dasar file output
        base_filename = simpledialog.askstring("Nama File", "Masukkan nama dasar untuk file output:")
        if not base_filename:
            messagebox.showerror("Error", "Nama file dasar tidak diberikan.")
            return

        # Membaca file CSV
        data = pd.read_csv(file_path)
        data_per_file = 200  # Jumlah data per file

        # Membagi data menjadi beberapa file
        for i in range(0, len(data), data_per_file):
            subset_data = data[i:i+data_per_file]
            output_file = f"{export_dir}/{base_filename}_part_{i//data_per_file + 1}.csv"
            subset_data.to_csv(output_file, index=False)

        messagebox.showinfo("Sukses", f"File berhasil dibagi dan disimpan di {export_dir}")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Membuat GUI
root = tk.Tk()
root.title("Split File CSV")

file_path = ""
export_dir = ""

# Antarmuka
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

file_label = tk.Label(frame, text="Tidak ada file yang dipilih.")
file_label.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

file_button = tk.Button(frame, text="Pilih File CSV", command=select_file)
file_button.grid(row=1, column=0, padx=5, pady=5)

folder_label = tk.Label(frame, text="Tidak ada folder yang dipilih.")
folder_label.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

folder_button = tk.Button(frame, text="Pilih Folder Output", command=select_output_folder)
folder_button.grid(row=3, column=0, padx=5, pady=5)

split_button = tk.Button(frame, text="Split File", command=split_file)
split_button.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()
