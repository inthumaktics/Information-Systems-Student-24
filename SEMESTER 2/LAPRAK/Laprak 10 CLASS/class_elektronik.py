#CLASS ELEKTRONIK
class elektronik:
    jumlah = 0
    def __init__(elekt, nama, jenis , harga):
        elekt.nama = nama
        elekt.jenis = jenis
        elekt.harga = harga
        elektronik.jumlah += 1

    def tampil_jumlah(elekt):
        print("Jumlah Elektronik %d : "), elektronik.jumlah

    def tampil_elektronik(elekt):
        print("Nama:", elekt.nama, ", Jenis : ", elekt.jenis, ", Harga:", elekt.harga)

elekt1 = elektronik("Ponsel", "Konsumen", 5000000)
elekt2 = elektronik("Mesin Cuci", "Rumah Tangga", 10000000)
elekt3 = elektronik("Kulkas", "Rumah Tangga", 10000000)
elekt4 = elektronik("Televisi", "Konsumen", 20000000)
elekt5 = elektronik("Kontrol Proses", "Industri", 150000000)
elektronik.jumlah

elekt1.tampil_elektronik()
elekt2.tampil_elektronik()
elekt3.tampil_elektronik()
elekt4.tampil_elektronik()
elekt5.tampil_elektronik()