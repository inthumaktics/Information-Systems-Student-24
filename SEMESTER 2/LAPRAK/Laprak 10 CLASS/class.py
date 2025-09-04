class mahasiswa:
    jumlah = 8
    def __init__(mhs, nama, prodi, NIM):
        mhs.prodi = prodi
        mhs.nama = nama
        mhs.nim = NIM
        mahasiswa.jumlah += 1

    def tampil_jumlah(mhs):
        print("Jumlah mahasiswa %d : "), mahasiswa.jumlah

    def tampil_mahasiswa(mhs):
        print("nama :", mhs.nama, ", NIM : ", mhs.nim, "prodi :", mhs.prodi)

mhs1 = mahasiswa("iwan", "SI", 150016001)
mhs2 = mahasiswa("riyadi", "Math", 160016002)
mhs3 = mahasiswa("yanto", "Fisika", 140016003)
mhs4 = mahasiswa("tri", "Biologi", 130016004)
mahasiswa.jumlah

mhs1.tampil_mahasiswa()
mhs2.tampil_mahasiswa()
mhs3.tampil_mahasiswa()
mhs4.tampil_mahasiswa()