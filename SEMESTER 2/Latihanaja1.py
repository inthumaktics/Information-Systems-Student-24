#LAPRAK1
#1. FUNGSI MENGHITUNG LUAS LINGKARAN 

def LuasLingkaran(r):
    'Fungsi menghitung Luas Lingkaran'
    phi = 22/7
    Luas = phi*(r**2)
    return Luas


r = int(input("Masukkan jari-jari lingkaran :"))
print(f"Luas lingkarannya adalah {LuasLingkaran(r)}")

#2. FUNGSI MENGHITUNG NILAI MINIMUM (nilai = [80, 75, 90, 88, 95])

def n_min(nilai):
    return min(nilai)

nilai = [80, 75, 90, 88, 95]
print(f"Nilai minimumnya adalah : {n_min(nilai)}")

#3. FUNGSI MENGHITUNG NILAI RATA-RATA (nilai = [80, 75, 90, 88, 95])
def n_rata_rata(nilai):
    jumlah = sum(nilai)
    banyak_data = len(nilai)
    rata_rata = jumlah / banyak_data
    return rata_rata

nilai = [80, 75, 90, 88, 95]
print(f"Nilai rata-ratanya adalah: {n_rata_rata(nilai)}")

#LAPRAK 2
#SEQUENTIAL SEARCH PRAKTIKUM

def sequentialsearch(data, key):
    pos = []
    for i in range(len(data)):
        if data[i]==key:
            pos.append(i+1)
    if len(pos)>0:
        print('data', key, 'sebanyak', len(pos), 'ditemukan di posisi', pos)
    else:
        print('data tidak ditemukan')
    return pos

data = [1, 3, 4, 5, 7, 8, 0, 1, 6, 2]
key = 7
print('Sequential Search')
sequentialsearch(data,key)

#BINARY SEARCH PRAKTIKUM
def binarysearch(data, key):
    awal = 1
    akhir = len(data) - 1
    ketemu = False
    
    while (awal<=akhir) and not ketemu:
        tengah = int((awal+akhir)/2)
        if key == data[tengah]:
            ketemu = True
            print('data', key, 'ditemukan di posisi', tengah)
        elif (key<data[tengah]):
            akhir=tengah-1
        else:
            awal=tengah+1
    if ketemu == False:
        print('data tidak ditemukan')


data = [1, 2, 5, 8, 10, 13, 15, 17, 19, 22, 25, 29, 30, 35, 40]
key = 29
print('Binary Search')
binarysearch(data, key)

#LAPRAK 3
#1. PENGURUTAN DATA SECARA DESCENDING
def insertion_sort_desc(sort_list):
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key > sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            print(f'pergeseran pada iterasi ke {i} j ke : {j} {sort_list}')
            j -= 1
        sort_list[j + 1] = key
        print(f'iterasi {i} {sort_list}')

A = [4, 3, 5, 6, 2, 78, 98]
insertion_sort_desc(A)

#2. MODIFIKASI 1 : 
def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            print('iterasi ke', i, sort_list)
            j -= 1
        sort_list[j + 1] = key
    print('iterasi', i-1 ,sort_list)


A=[4,3,5,6,2,78,98]
insertion_sort(A)
#3. MODIFIKASI 2 : 
def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            print(f'pergeseran pada iterasi ke {i} j ke : {j} {sort_list}')
            j -= 1
        sort_list[j + 1] = key
        print(f'iterasi {i} {sort_list}')

A = [4, 3, 5, 6, 2, 78, 98]
insertion_sort(A)

#LAPRAK 4
#1. Pengurutan secara Descending : 
def Selection_sort(A):
    for i in range(len(A)):
        print("---------------------")
        print(f"List sebelum penukaran {i}: {A}")
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] < A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]

A = [5, 11, 2, 47, 144, 1, 25]
Selection_sort(A)
print("---------------------")
print(f'Hasil Akhir pengurutan secara Descending : {A}')

#2. Modifikasi pengurutan : 
def Selection_sort(A):
    for i in range(len(A)):
        print("---------------------")
        print(f"Iterasi {i} : {A}")
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] < A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]

A = [5, 11, 2, 47, 144, 1, 25]
Selection_sort(A)
print("---------------------")
print(f'Hasil Akhir pengurutan secara Descending : {A}')

#LAPRAK 5
#1. MODIFIKASI PENGURUTAN DATA SECARA DESCENDING 

def buble2(A):
    tukar = True
    while tukar:
        tukar = False
        for j in range(len(A)-1):
            if A[j]<A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                print(f"tukar {A[j]} dengan {A[j+1]}")
                print(f"urutan menjadi {A}")
                tukar = True
    return A
    
A = [3, 1, 8, 4, 2]

print(f"HASIL AKHIR URUTANNYA ADALAH {buble2(A)}")

#2. MODIFIKASI FUNGSI MENAMPILKAN HASIL TIAP LANGKAH PENGURUTAN : 

def buble2(A):
    tukar = True
    while tukar:
        tukar = False
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                print(f"tukar {A[j]} dengan {A[j+1]}")
                print(f"urutan menjadi {A}")
                tukar = True
    return A
    
A = [3, 1, 8, 4, 2]

print(f"HASIL AKHIR URUTANNYA ADALAH {buble2(A)}")

#LAPRAK 6
#KASUS REKURSIF FIBONACI : 
def fib(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
fib(7)
print(f"Hasil rekursinya : {fib(10)}")
#1. UBAH FUNGSI FIBONACI DALAM BENTUK ITERASI : 
# LOOP FOR :
def fib_for(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else : 
        a, b = 0,1
        for i in range(2, n+1):
            sum_fib = a + b
            a = b
            b = sum_fib
        return b

fib_for(7)
print(f"Hasil rekursinya : {fib_for(7)}")
# LOOP WHILE : 
def fib_while(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a, b = 0, 1
        count = 2
        while count <= n:
            sum_fib = a + b
            a = b
            b = sum_fib
            count += 1
        return b
        
fib_while(7)
print(f"Hasil rekursinya : {fib_while(7)}")
# B. PROGRAM MENGHITUNG REKURSINYA : 
def rek_pangkat_2(x):
    if x == 0 :
        return 1
    elif x < 0 :
        return 1
    else : 
        return 2 * rek_pangkat_2(x-1)
        
rek_pangkat_2(20)
print(f"Hasil rekursinya : {rek_pangkat_2(20)}")
# C. PROGRAM DENGAN ITERASI/PERULANGAN : 
def iter_pangkat_2(x):
    if x == 0:
        return 1
    elif x < 0: 
        hasil = 1.0
        for i in range(abs(x)):
            hasil /= 2         
        return hasil
    else:       
        hasil = 1
        for i in range(x):
            hasil *= 2    
        return hasil
        
iter_pangkat_2(20)
print(f"Hasil rekursinya : {iter_pangkat_2(20)}")

#LAPRAK 7
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian dengan nol!"

def kalkulator():
    print("Kalkulator Sederhana")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    print("5. Keluar")

    while True:
        pilihan = input("\nMasukkan pilihan (1/2/3/4/5): ")
        
        if pilihan == '5':
            print("Keluar dari kalkulator...")
            break
            
        if pilihan in ('1', '2', '3', '4'):
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Error: Masukkan angka yang valid!")
                continue
            
            if pilihan == '1':
                print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
            elif pilihan == '2':
                print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
            elif pilihan == '3':
                print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
            elif pilihan == '4':
                print(f"Hasil: {angka1} / {angka2} = {bagi(angka1, angka2)}")
        else:
            print("Pilihan tidak valid!")

# Jalankan kalkulator
kalkulator()

#LAPRAK8 
#KALKULATOR PENGEMBALIAN INVESTASI 

def calculate_profit_and_roi():
    print("Kalkulator Pengembalian Investasi")
    print("---------------------------------")
    
#INPUT DANA YANG DIINVESTASIKAN : 
    while True:
        try:
            total_costs_input = input("Masukkan jumlah total yang diinvestasikan/dibelanjakan (Total Biaya): ")
            total_costs = float(total_costs_input)
            if total_costs < 0:
                print("Total biaya tidak boleh negatif. Silakan masukkan angka positif.")
            else:
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka untuk total biaya.")

#INPUT TOTAL PEROLEHAN DARI INVESTASI :
    while True:
        try:
            total_sales_input = input("Masukkan jumlah total yang diperoleh (Total Penjualan): ")
            total_sales = float(total_sales_input)
            if total_sales < 0:
                print("Total penjualan tidak boleh negatif. Silakan masukkan angka positif.")
            else:
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka untuk total penjualan.")

#MENGHITUNG UNTUNG/RUGI :
    profit = total_sales - total_costs

    print("\n--- Hasil Perhitungan ---")
    print(f"Total Biaya: Rp {total_costs:,.2f}")
    print(f"Total Penjualan: Rp {total_sales:,.2f}")

 #MENAMPILKAN HASIL UNTUNG/RUGI : 
    if profit > 0:
        print(f"Laba: Rp {profit:,.2f} (Untung!)")
    elif profit < 0:
        print(f"Rugi: Rp {abs(profit):,.2f} (Rugi!)")
    else:
        print("Laba/Rugi: Rp 0.00 (Titik impas!)")


#KALKULATOR ROI : 
    if total_costs == 0:
        print("Tidak dapat menghitung ROI karena total biaya adalah nol.")
    else:
        roi = (profit / total_costs) * 100
        print(f"Pengembalian Investasi (ROI): {roi:.2f}%")

#MENJALANKAN KALKULATOR : 
if __name__ == "__main__":
    calculate_profit_and_roi()

#LAPRAK 9
#MODULE FUNGSI PERHITUNGAN 

#PENJUMLAHAN :
def penjumlahan(a, b):  
    print("Hasil Penjumlahan dari:", a, '+', b, '=', a + b)

#PENGURANGAN :
def Pengurangan(a, b):
    print("Hasil Pengurangan dari:", a, '-', b, '=', a - b)

#PERKALIAN :
def Perkalian(a, b):
    print("Hasil Pengurangan dari:", a, '*', b, '=', a * b)

#PEMBAGIAN :
def Pembagian(a, b):
    print("Hasil Pembagian dari:", a, '/', b, '=', a / b)

# #PEMANGGILAN 1
# import ModulePerhitungan as hitung

# hitung.penjumlahan(20, 10)
# hitung.Pengurangan(30, 20)
# hitung.Perkalian(45, 7)
# hitung.Pembagian(100, 5)

# print("="*40)
# #PEMANGGILAN 2
# from ModulePerhitungan import penjumlahan as t, Pengurangan as k, Perkalian as kl, Pembagian as bg

# t(20, 20)
# k(100, 10)
# kl(50, 5)
# bg(70, 3)

#LAPRAK 10
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