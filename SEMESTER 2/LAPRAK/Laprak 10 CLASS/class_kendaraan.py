#CLASS KENDARAAN

class Kendaraan:
    jumlah = 0
    def __init__(kend, nama, jenis , harga):
        kend.nama = nama
        kend.jenis = jenis
        kend.harga = harga
        Kendaraan.jumlah += 1

    def tampil_jumlah(kend):
        print("Jumlah Kendaraan %d : "), Kendaraan.jumlah

    def tampil_Kendaraan(kend):
        print("Nama:", kend.nama, ", Jenis : ", kend.jenis, ", Harga:", kend.harga)

kend1 = Kendaraan("Sepeda Motor", "Bermotor", 120000000)
kend2 = Kendaraan("Mobil", "Bermotor", 550000000)
kend3 = Kendaraan("Sepeda", "Tidak Bermotor", 6000000)
kend4 = Kendaraan("Delman", "Tidak Bermotor", 75000000)
kend5 = Kendaraan("Kereta Api", "Bermotor", 20000000000)
Kendaraan.jumlah

kend1.tampil_Kendaraan()
kend2.tampil_Kendaraan()
kend3.tampil_Kendaraan()
kend4.tampil_Kendaraan()
kend5.tampil_Kendaraan()
