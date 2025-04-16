print("=====1. Mencari huruf a pada nama=====")

nama_saya = input("Masukkan nama saya : ")
huruf_kecil = nama_saya.lower()
jumlah_a = huruf_kecil.count('a')

print("Jumlah huruf 'a' di dalam nama Saya adalah :", jumlah_a)

print("=====2. Memisahkan lalu Menggabungkan nama-nama=====")

text = "Agus, Gus, Budi, Yayan"
pisahkan = text.split(",")
gabungkan = ' dan '.join(pisahkan)

print("Hasil pisahkan nama-nama :", pisahkan)
print("Outputnya adalah :", gabungkan)

print("=====3. Mengubah huruf a di teks menjadi i")

kalimat = "Saya adalah warga Indonesia"
kalimat_baru = kalimat.replace("a", "i")

print("Outputnya adalah :", kalimat_baru)