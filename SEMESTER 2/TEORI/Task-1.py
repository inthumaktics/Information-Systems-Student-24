'''Tantangan mengerjakan soal hasil kerja sendiri vs soal hasil kerja AI '''

'''SOAL TANTANGAN 1 : Menampilkan informasi (uang yang terkumpul)'''

###Hasil kerja sendiri : 
print("Order Kue Di sini : ")
print('''
Kue yang Tersedia dan Harganya : 
1. Cupcake = 40P
2. Macarons = 50P
3. Cheesecake = 70P
''')

### Program order : 
while True :
    jumlah_1 = 0
    jumlah_2 = 0
    jumlah_3 = 0
    pesan = (input("Masukkan kode kue yang ingin anda pesan (1, 2, atau 3) : "))
    # jumlah = int(input("Berapa banyak kue yang ingin anda pesan (5, 10, atau 20 ) :"))

    if pesan == '1':
        jumlah_1 = int(input("Berapa banyak kue yang ingin anda pesan (5, 10, atau 20 ) :"))
        jumlah_1 = jumlah_1*40
        print(f"Jumlah Pesanan Kue anda : {jumlah_1}")
    elif pesan == '2':
        jumlah_2 = int(input("Berapa banyak kue yang ingin anda pesan (5, 10, atau 20 ) :"))
        jumlah_2 = jumlah_2*50
        print(f"Jumlah Pesanan Kue anda : {jumlah_2}")
    elif pesan == '3':
        jumlah_3 = int(input("Berapa banyak kue yang ingin anda pesan (5, 10, atau 20 ) :"))
        jumlah_3 = jumlah_3*70
        print(f"Jumlah Pesanan Kue anda : {jumlah_3}")
    else :
        print(f"Maaf kode tidak valid!")
        continue
    print(f"Total Pesanan Kue anda : {jumlah_1+jumlah_2+jumlah_3}")

    ulang = input("Apakah ingin memesan lagi? (y/n) : ")
    if ulang != 'y':
        print("Terima kasih telah memesan!")
        break

### Program hasil penjualan : 
print("Pilihan Hasil Penjualan : ")
print('''
Kue yang Tersedia dan Harganya : 
1. Cupcake = 40P
2. Macarons = 50P
3. Cheesecake = 70P
4. Total Semua Kue
''')

hasil_jual = input("Menampilkan hasil penjualan kue (1, 2, 3, 4) :")

if hasil_jual == '1': 
    print(f"Hasil Penjualan Kue Cupcake : {jumlah_1}")
elif hasil_jual == '2':
    print(f"Hasil Penjualan Kue Macarons : {jumlah_2}")
elif hasil_jual == '3':
    print(f" Hasil Penjualan Kue Cheesecake : {jumlah_3}")
elif hasil_jual == '4':
    print(f"Hasil Penjualan Semua Kue : {jumlah_1+jumlah_2+jumlah_3}")
else :
    print("Salah input! ulangi!")


###HASIL KERJA AI : 
# Mendefinisikan harga per jenis kue
harga_cupcake = 40
harga_macaron = 50
harga_cheesecake = 70

# Meminta input jumlah kue yang terjual
jumlah_cupcake = int(input("Masukkan jumlah cupcake yang terjual: "))
jumlah_macaron = int(input("Masukkan jumlah macaron yang terjual: "))
jumlah_cheesecake = int(input("Masukkan jumlah cheesecake yang terjual: "))

# Menghitung total uang yang terkumpul
total_pendapatan = (jumlah_cupcake * harga_cupcake) + (jumlah_macaron * harga_macaron) + (jumlah_cheesecake * harga_cheesecake)

# Menampilkan hasil
print(f"Total uang yang terkumpul adalah {total_pendapatan} pence.")

#JAWABAN TANTANGAN 1 : 
a = int(input("Jumlah cupcake terjual : "))
b = int(input("Jumlah macaron terjual : "))
c = int(input("Jumlah cheesecake terjual : "))
uang_terkumpul = (a * 40) + (b * 50) + (c * 70)
print(uang_terkumpul)

#function : 
def cupcake(a,b,c):
    Uang = (40*a)+(50*b)+(70*c)
    return Uang