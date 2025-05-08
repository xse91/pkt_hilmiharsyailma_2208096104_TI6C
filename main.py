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