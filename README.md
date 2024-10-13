**TUGAS TERDISTRIBUSI**

Miranda BM Sigalingging (320220401015)

Sufi Naylil Karomah (320220401024)

**I. CLIENT-SERVER COMMUNICATION**

**DESKRIPSI**
Mengimplementasikan sistem komunikasi client-server dengan fitur load balancing. Berikut deskripsi singkat untuk setiap bagian:

1. Client:
- Membuat koneksi ke load balancer di port 2220.
- Mengirim pesan ke server dan menerima balasan.
- Menghitung latensi, response time, dan throughput untuk setiap transaksi.
- Mendukung multiple clients menggunakan threading untuk menjalankan hingga 100 klien secara paralel.

2. Load Balancer:
- Mendengarkan di port 2220 untuk menerima koneksi dari klien.
- Mendistribusikan pesan secara bergantian (round-robin) ke server yang berjalan di port 2221, 2222, dan 2223.
- Mengirim pesan dari klien ke server dan mengirimkan balasan kembali ke klien.

3. Server:
- Tiga server berjalan secara paralel pada port 2221, 2222, dan 2223.
- Menerima pesan dari load balancer, mencatat aktivitas ke file log, dan mengirimkan balasan ke klien.
- Setiap server menggunakan thread untuk menangani banyak koneksi klien secara bersamaan.

**II. PEER 2 PEER**

Dalam jaringan P2P ini, setiap node bertindak sebagai server dan client, di mana node dapat menyimpan file, mencari file di node lain, dan mengirim file kepada node yang memintanya. Program ini mendukung dua algoritma pencarian file, yaitu flooding dan random walk.
**Komponen Utama:**
a. Kelas Node:

Setiap instance dari kelas Node merepresentasikan satu node dalam jaringan P2P. Node ini memiliki kemampuan untuk:
Menjalankan server UDP untuk menerima pesan dari node lain.
Menyimpan file dalam bentuk dictionary, di mana nama file menjadi kunci dan isi file menjadi nilainya.
Mengirim permintaan pencarian atau permintaan file ke node lain.

b. Pencarian File:

Node dapat mencari file di jaringan menggunakan salah satu dari dua metode berikut:
Flooding: Node akan mengirimkan permintaan pencarian ke semua node yang dikenal secara langsung. Setiap node yang menerima permintaan ini akan memeriksa apakah file yang diminta tersedia, dan jika tidak, mereka akan meneruskan permintaan ke node-node lainnya.
Random Walk: Node mengirimkan permintaan pencarian ke satu node acak dari daftar node yang dikenal. Jika file tidak ditemukan, permintaan diteruskan ke node lain secara acak hingga file ditemukan atau batas waktu habis.

c. Pengukuran Performa:

Program mencatat waktu respons (response time) dan throughput selama proses pencarian file, yang dihitung berdasarkan ukuran file dan waktu pencarian. Hal ini berguna untuk mengukur efektivitas dari masing-masing metode pencarian.

**Alur Program:**
- Pengguna diminta untuk menentukan jumlah node yang akan dibuat (5, 10, atau 20).
- Setiap node diinisialisasi dengan alamat host dan port yang berbeda, dan server UDP pada masing-masing node mulai mendengarkan koneksi.
- Node dapat menambahkan file (latihan.txt sebagai contoh) untuk dibagikan di jaringan.
- Pengguna memilih metode pencarian file: flooding atau random walk.
- Node akan mencari file yang diinginkan menggunakan metode pencarian yang dipilih dan mengukur performa pencarian.

**Fitur Utama:**
* Komunikasi UDP: Setiap node menggunakan socket UDP untuk mengirim dan menerima pesan pencarian atau permintaan file dari node lain.
* Asynchronous Listening: Setiap node mendengarkan pesan dari node lain di thread terpisah, sehingga dapat menangani beberapa permintaan secara paralel.
* Dua Metode Pencarian:
Flooding: Mengirim permintaan ke semua node yang dikenal.
Random Walk: Mengirim permintaan secara acak ke satu node pada satu waktu.
* Pengukuran Performa: Mencatat waktu respons dan throughput selama proses pencarian file.

