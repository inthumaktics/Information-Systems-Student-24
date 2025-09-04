class matakuliah:
    jumlah = 0
    def __init__(matkul, nama_matkul, SKS, kode):
        matkul.nama_matkul = nama_matkul
        matkul.SKS = SKS
        matkul.kode = kode
        matakuliah.jumlah += 1


    def tampil_jumlah(matkul):
        print("Jumlah mata kuliah %d : "), matakuliah.jumlah

    def tampil_matkul(matkul):
        print("Nama Mata kuliah :", matkul.nama_matkul, ", SKS : ", matkul.SKS, "Kode :", matkul.kode)

matkul1 = matakuliah("Algoritma Pemrograman", 3, 245001)
matkul2 = matakuliah("SI Manajemen", 3, 245002)
matkul3 = matakuliah("Analisis Proses Bisnis", 3, 245003)
matkul4 = matakuliah("Konsep Basis Data", 3, 245004)
matakuliah.jumlah

matkul1.tampil_matkul()
matkul2.tampil_matkul()
matkul3.tampil_matkul()
matkul4.tampil_matkul()