# Kelompok 3
# 1. Hilmi Harsya Ilma
# 2. Edo Maulana
# 3. Nasril Nizar
# 4. Rasyid Syahrindra Endwin

Program di atas adalah sistem deteksi gerakan yang menggunakan modul GPIO (General Purpose Input/Output). Program ini mendeteksi gerakan melalui sensor yang terhubung ke pin digital dan memberikan respons berupa mengaktifkan perangkat output. Berikut penjelasan detail tentang cara kerja program:
Komponen Utama Program:

1. Import Library:

  - gpio: Modul untuk mengakses dan mengontrol pin GPIO pada perangkat
  - time: Modul untuk fungsi delay dan kontrol waktu


2. Fungsi sensorGerakan():

  - Fungsi ini berfungsi sebagai callback yang akan dijalankan ketika terjadi perubahan pada sensor
  - Membaca status sensor gerakan melalui pin digital 0
  - Jika nilai = 0: tidak ada gerakan terdeteksi, mematikan output pada pin 1 dan 2
  - Jika nilai = 1: ada gerakan terdeteksi, menyalakan output pada pin 1 dan 2


3. Fungsi main():

  - Mendaftarkan event detector pada pin 0 yang akan memanggil fungsi sensorGerakan()
  - Menjalankan loop tak terbatas agar program terus berjalan
  - Memberikan delay 100ms untuk mengurangi penggunaan CPU

4. Blok Eksekusi Utama:

  - Memeriksa apakah program dijalankan sebagai program utama
  - Ada kesalahan kecil di kode asli, yang telah diperbaiki di kode yang dikomentari

Cara Kerja Sistem:

  - Ketika program dijalankan, sistem akan terus memantau sensor gerakan
  - Jika ada gerakan terdeteksi, perangkat output (LED, buzzer, atau perangkat lain) pada pin 1 dan pin 2 akan menyala
  - Jika tidak ada gerakan, perangkat output akan dimatikan
  - Program terus berjalan dalam loop tak terbatas
