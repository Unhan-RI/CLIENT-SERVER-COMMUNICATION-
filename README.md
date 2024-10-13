**TUGAS TERDISTRIBUSI / CLIENT-SERVER COMMUNICATION**

Miranda BM Sigalingging (320220401015)

Sufi Naylil Karomah (320220401024)

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
