import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Menampilkan file picker untuk memilih file CSV
Tk().withdraw()  # Menyembunyikan jendela utama Tkinter
file_path = askopenfilename(title="Pilih file CSV", filetypes=[("CSV Files", "*.csv")])

# Pastikan file dipilih
if file_path:
    # Membaca file CSV yang dipilih
    data = pd.read_csv(file_path)

    # Tentukan jumlah data per file
    data_per_file = 200

    # Loop untuk membagi data menjadi beberapa file
    for i in range(0, len(data), data_per_file):
        subset_data = data[i:i+data_per_file]
        subset_data.to_csv(f'customer_data_part_{i//data_per_file + 1}.csv', index=False)

    print(f'File berhasil dibagi menjadi beberapa bagian.')
else:
    print("Tidak ada file yang dipilih.")
