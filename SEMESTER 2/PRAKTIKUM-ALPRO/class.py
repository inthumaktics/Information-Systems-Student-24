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

