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
