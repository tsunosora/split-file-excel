import pandas as pd

# Ganti file_path sesuai dengan lokasi file CSV Anda
file_path = r'D:\WA BLAST\UPDATE TOOL 28-08-24\HASIL SCRAPTING\Perusahaan Konstruksi\extracted_Perusahaan Konstruksi.csv'
data = pd.read_csv(file_path)

# Tentukan jumlah data per file
data_per_file = 200

# Loop untuk membagi data menjadi beberapa file
for i in range(0, len(data), data_per_file):
    subset_data = data[i:i+data_per_file]
    subset_data.to_csv(f'customer_data_part_{i//data_per_file + 1}.csv', index=False)
