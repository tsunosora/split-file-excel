import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.simpledialog import askstring

# Menampilkan file picker untuk memilih file CSV
Tk().withdraw()  # Menyembunyikan jendela utama Tkinter
file_path = askopenfilename(title="Pilih file CSV", filetypes=[("CSV Files", "*.csv")])

# Pastikan file dipilih
if file_path:
    # Menampilkan dialog untuk memilih direktori tujuan export
    export_dir = askdirectory(title="Pilih folder untuk menyimpan file hasil")

    # Pastikan direktori dipilih
    if export_dir:
        # Meminta nama file dasar untuk output
        base_filename = askstring("Nama File", "Masukkan nama dasar untuk file output:")

        # Memastikan nama file diberikan
        if base_filename:
            # Membaca file CSV yang dipilih
            data = pd.read_csv(file_path)

            # Tentukan jumlah data per file
            data_per_file = 200

            # Loop untuk membagi data menjadi beberapa file
            for i in range(0, len(data), data_per_file):
                subset_data = data[i:i+data_per_file]
                # Menentukan nama file output berdasarkan nama dasar dan nomor bagian
                output_file = f'{export_dir}/{base_filename}_part_{i//data_per_file + 1}.csv'
                subset_data.to_csv(output_file, index=False)

            print(f'File berhasil dibagi dan disimpan di {export_dir}')
        else:
            print("Nama file dasar tidak diberikan.")
    else:
        print("Direktori tujuan tidak dipilih.")
else:
    print("Tidak ada file yang dipilih.")
