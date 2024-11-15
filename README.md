**Penjelasan Kode**
1. Menggunakan pd.read_csv() untuk membaca file CSV.
2. Menggunakan to_csv() untuk menyimpan setiap bagian dengan 200 data sebagai file CSV baru.
3. Nama file yang dihasilkan akan berupa customer_data_part_1.csv, customer_data_part_2.csv, dan seterusnya.
Pastikan file CSV Anda berada di lokasi yang benar, dan sesuaikan file_path jika perlu.

**Penjelasan tkinter:**
1. Menggunakan tkinter untuk membuka dialog file picker, yang memungkinkan Anda memilih file CSV secara manual.
2. Setelah memilih file, data akan dibaca dengan pd.read_csv().
3. File kemudian akan dibagi menjadi beberapa bagian (200 data per file) dan disimpan sebagai file CSV baru.
4. Hasilnya akan berupa file CSV yang dinamai customer_data_part_1.csv, customer_data_part_2.csv, dan seterusnya.

**Penjelasan Penambahan Pilih Output File**:
1.	Pemilihan File Input:
o	Menggunakan askopenfilename() untuk memilih file CSV yang ingin diproses.
2.	Pemilihan Direktori Export:
o	Menggunakan askdirectory() untuk memilih folder tempat file hasil pembagian akan disimpan.
3.	Penyimpanan File Hasil:
o	Setiap bagian data disimpan dalam file CSV di folder yang dipilih, dengan nama customer_data_part_1.csv, customer_data_part_2.csv, dan seterusnya.

**Cara Kerja:**
1.	Program akan meminta Anda memilih file CSV yang ingin dibagi.
2.	Setelah itu, Anda akan diminta memilih folder untuk menyimpan file hasil.
3.	File akan dibagi menjadi beberapa bagian, dan setiap bagian disimpan di folder yang Anda pilih.
