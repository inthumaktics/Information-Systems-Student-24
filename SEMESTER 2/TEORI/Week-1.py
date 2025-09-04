'''REVIEW DASAR PEMROGRAMAN SEMESTER 1'''

'''1. Menghitung Keliling Persegi '''

S = int(input("Masukkan sisi persegi :"))
K = 4*S

print(f"Keliling persegi ={K}")

'''2. Program membantu Dosen dalam melakukan presensi'''

daftar_mhs = ['mhs1', 'mhs2', 'mhs3', 'mhs4', 'mhs5', 'mhs5', 'mhs6', 'mhs7', 'mhs8', 'mhs9', 'mhs10']
hitung = 0
hadir = 0

for mhs in daftar_mhs:
    print('Nama Mahasiswa', mhs)
    hitung = hitung+1
    presensi = input("apakah mahasiswa hadir? (y/t) :")
    if presensi == 'y':
        hadir =  hadir+1
print(f"Jumlah mahasiswa : {hitung}")
print(f"Jumlah yang hadir : {hadir}")
absen = hitung - hadir
print(f"Jumlah tidak hadir: {absen}")


'''3. Menghitung tiket masuk Aqua Park'''

A = int(input("Jumlah tiket dewasa :"))
B = int(input("Jumlah tiket anak :"))
Harga = A*15 + B*11
print(Harga)
if Harga > 50 :
    Harga = Harga - Harga * 5/100
else : 
    Harga = Harga