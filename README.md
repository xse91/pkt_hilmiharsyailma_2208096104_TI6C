# Kelompok 3
# 1. Hilmi Harsya Ilma
# 2. Edo Maulana
# 3. Nasril Nizar
# 4. Rasyid Syahrindra Endwin

# Import library yang diperlukan
from gpio import *    # Mengimpor semua fungsi dari modul gpio untuk mengakses pin GPIO
from time import *    # Mengimpor semua fungsi dari modul time untuk fungsi delay

# Fungsi callback yang akan dipanggil ketika ada perubahan pada sensor gerakan
def sensorGerakan():
    # Membaca nilai dari pin digital 0 (sensor gerakan)
    nilai = digitalRead(0)
    
    # Cek status sensor gerakan
    if nilai == 0:
        # Jika nilai = 0, berarti tidak ada gerakan terdeteksi
        print("Tidak ada gerakan!")
        customWrite(1, 0)    # Matikan perangkat pada pin 1 (mungkin LED)
        customWrite(2, 0)    # Matikan perangkat pada pin 2 (mungkin buzzer atau relay)
    else:
        # Jika nilai = 1, berarti ada gerakan terdeteksi
        print("Ada gerakan!")
        customWrite(1, 1)    # Nyalakan perangkat pada pin 1
        customWrite(2, 1)    # Nyalakan perangkat pada pin 2

# Fungsi utama program
def main():
    # Daftarkan event detector pada pin 0, yang akan memanggil fungsi sensorGerakan
    # ketika ada perubahan pada pin sensor
    add_event_detect(0, sensorGerakan)
    
    # Loop utama program agar terus berjalan
    while True:
        delay(100)    # Delay 100 milidetik untuk mengurangi beban CPU

# Cek apakah program dijalankan sebagai program utama
# Ada perbaikan: seharusnya '__main__' (dengan double underscore)
if __name__ == "__main__":
    main()    # Jalankan fungsi main


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
