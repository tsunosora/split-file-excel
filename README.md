## Penjelasan Kode
* Menggunakan pd.read_csv() untuk membaca file CSV.
* Menggunakan to_csv() untuk menyimpan setiap bagian dengan 200 data sebagai file CSV baru.
* Nama file yang dihasilkan akan berupa customer_data_part_1.csv, customer_data_part_2.csv, dan seterusnya.
Pastikan file CSV Anda berada di lokasi yang benar, dan sesuaikan file_path jika perlu.

## Penjelasan tkinter
1. Menggunakan tkinter untuk membuka dialog file picker, yang memungkinkan Anda memilih file CSV secara manual.
2. Setelah memilih file, data akan dibaca dengan pd.read_csv().
3. File kemudian akan dibagi menjadi beberapa bagian (200 data per file) dan disimpan sebagai file CSV baru.
4. Hasilnya akan berupa file CSV yang dinamai customer_data_part_1.csv, customer_data_part_2.csv, dan seterusnya.

## Penjelasan Penambahan Pilih Output File
1. Pemilihan File Input:
* Menggunakan askopenfilename() untuk memilih file CSV yang ingin diproses.
2. Pemilihan Direktori Export:
* Menggunakan askdirectory() untuk memilih folder tempat file hasil pembagian akan disimpan.
3. Penyimpanan File Hasil:
*	Setiap bagian data disimpan dalam file CSV di folder yang dipilih, dengan nama customer_data_part_1.csv, customer_data_part_2.csv, dan seterusnya.

## Cara Kerja
1.	Program akan meminta Anda memilih file CSV yang ingin dibagi.
2.	Setelah itu, Anda akan diminta memilih folder untuk menyimpan file hasil.
3.	File akan dibagi menjadi beberapa bagian, dan setiap bagian disimpan di folder yang Anda pilih.


# Penjelasan Kode:
1.	Pemilihan File Input:
askopenfilename() digunakan untuk memilih file CSV yang ingin dibagi.
2.	Pemilihan Direktori Export:
askdirectory() digunakan untuk memilih folder tempat file hasil akan disimpan.
3.	Input Nama File Output:
askstring() digunakan untuk meminta input nama dasar file output dari pengguna. Nama file ini akan digunakan untuk setiap bagian hasil split, dengan nomor bagian ditambahkan di belakangnya (misalnya, customer_data_part_1.csv).
4.	Penyimpanan File Hasil:
File dibagi sesuai jumlah baris yang ditentukan (200 data per file) dan disimpan di folder yang dipilih dengan nama dasar yang ditentukan.

## Cara Kerja:
1.	Program akan meminta Anda memilih file CSV yang ingin dibagi.
2.	Kemudian, Anda akan diminta memilih folder untuk menyimpan file hasil.
3.	Selanjutnya, Anda akan diminta memasukkan nama dasar untuk file output. Nama file hasil akan mengikuti pola nama_file_dasar_part_X.csv.
4.	File akan dibagi menjadi beberapa bagian, dan setiap bagian disimpan di folder yang Anda pilih dengan nama yang sudah disesuaikan.
Sekarang Anda bisa mengganti nama file output dan memilih folder tujuan secara fleksibel!

