'''IF-ELIF-ELSE TO SWITCH CASE'''

#1. Program menentukan jenis kendaraan berdasarkan kode kendaraan yang dimasukkan :
print("Kode kendaraan : M, MOB, dan B")

###IF-ELIF-ELSE :
kendaraan = input("Masukkan Kode Kendaraan :")
if kendaraan == "M":
    print("Motor")
elif kendaraan == "MOB" :
    print("Mobil")
elif kendaraan == "B" :
    print("Bus")
else :
    print("Salah input! coba lagi!")

###SWITCH CASE :
def jenis_kendaraan(kendaraan):
    switch = {
        'M': 'Motor',
        'MOB': 'Mobil',
        'B': "Bus"
    }
    return switch.get(kendaraan, "Salah input! coba lagi!")
print(jenis_kendaraan(kendaraan))

#2. Program menampilkan nama musim berdasarkan nomor musim :

print("Nomor Musim : 1, 2, 3, dan 4")

###IF-ELIF-ELSE:
musim = int(input("Masukkan nomor musim :"))

if musim == 1 :
    print("Musim Semi")
elif musim == 2:
    print("Musim Panas")
elif musim == 3:
    print("Musim Gugur")
elif musim == 4 :
    print("Musim Dingin")
else :
    print("Salah input! coba lagi!")

###SWITCH CASE :
def jenis_musim(musim):
    switch = {
        1: 'Musim Semi',
        2: 'Musim Panas',
        3: 'Musim Gugur',
        4: 'Musim Dingin'
    }
    return switch.get(musim, "Salah input! coba lagi!")
print(jenis_musim(musim))


#3. Program menentukan kategori tiket berdasarkan kode kelas :
print("Kode kelas tiket : EK, BS, dan FR")

###IF-ELIF-ELSE: 
tiket = input("Masukkan kode kelas tiket : ")

if tiket == 'EK' :
    print("Ekonomi")
elif tiket == 'BS':
    print("Bisnis")
elif tiket == 'FR':
    print("First class")

###SWITCH CASE :

def kelas_tiket(tiket):
    switch = {
        'EK': 'Ekonomi',
        'BS': 'Bisnis',
        'FR': 'First class'
    }
    return switch.get(tiket, "Salah input! coba lagi!")
print(kelas_tiket(tiket))