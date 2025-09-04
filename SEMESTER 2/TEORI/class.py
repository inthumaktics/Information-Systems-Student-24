# class mahasiswa:
#     jumlah = 0
#     def __init__(mhs, nama, prodi, NIM):
#         mhs.prodi = prodi
#         mhs.nama = nama
#         mhs.NIM = NIM
#         mahasiswa.jumlah + 1
    
#     def tampil_jumlah(mhs):
#         print("Jumlah mahasiswa %d :", mahasiswa.jumlah)

#     def tampil_mahasiswa(mhs):
#         print("nama : ", mhs.nama, "NIM :", mhs.nim, "prodi :", mhs.prodi)

class mahasiswa:
    jumlah = 0
    def __init__(mhs, nama, prodi, NIM):
        mhs.prodi = prodi
        mhs.nama = nama
        mhs.NIM = NIM
        mahasiswa.jumlah + 1
    
    def tampil_jumlah(mhs):
        print("Jumlah mahasiswa %d :", mahasiswa.jumlah)

    def tampil_mahasiswa(mhs):
        print("nama : ", mhs.nama, "NIM :", mhs.nim, "prodi :", mhs.prodi)
    
        return
        
mhs1 = mahasiswa("iwan", "SI", 150016001)
mhs2 = mahasiswa("riyadi", "Math", 160016002)
mhs3 = mahasiswa("yanto", "Fisika", 140016003)
mhs4 = mahasiswa("tri", "Biologi", 130016004)

# tampil_mahasiswa(mhs1)
# tampil_mahasiswa(mhs2)