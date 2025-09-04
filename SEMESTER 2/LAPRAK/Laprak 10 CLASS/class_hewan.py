#CLASS HEWAN
class hewan:
    jumlah = 0
    def __init__(anml, nama_hewan, kelas, t_hidup):
        anml.nama_hewan = nama_hewan
        anml.kelas = kelas
        anml.t_hidup = t_hidup
        hewan.jumlah += 1

    def tampil_jumlah(anml):
        print("Jumlah Hewan %d : "), hewan.jumlah

    def tampil_hewan(anml):
        print("Nama Hewan:", anml.nama_hewan, ", Kelas Hewan : ", anml.kelas, ", Tempat Hidup:", anml.t_hidup)

anml1 = hewan("Kucing", "Mamalia", "Darat")
anml2 = hewan("Kuda", "Mamalia", "Darat")
anml3 = hewan("Pinguin", "Aves", "Air")
anml4 = hewan("Paus", "Mamalia", "Air")
anml5 = hewan("Merpati", "Aves", "Darat")
hewan.jumlah

anml1.tampil_hewan()
anml2.tampil_hewan()
anml3.tampil_hewan()
anml4.tampil_hewan()
anml5.tampil_hewan()