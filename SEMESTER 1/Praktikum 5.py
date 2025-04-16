#1. MEMBUAT PROGRAMN MEMINTA PENGGUNA UNTUK MEMASUKKAN ANGKA SEBANYAK N KALI

N = int(input("Masukkan N: "))

jumlah = 0
angka_list = []

for i in range(N):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    angka_list.append(angka)  
    jumlah += angka 

angka_str = ' + '.join(map(str, angka_list))

print(f"{angka_str} = {jumlah}")

#2. MENGHITUNG TOTAL RATA-RATA DARI SEMUA ANGKA YANG DIMASUKKAN 
N = int(input("Masukkan N: "))

jumlah = 0

for i in range(N):
    angka = float(input(f"Masukkan angka ke-{i+1}: "))  
    jumlah += angka 

rata_rata = jumlah / N

print(f"Total: {jumlah}")
print(f"Rata-rata: {rata_rata}")

if rata_rata > 50:
    print("Rata-rata di atas 50")
else:
    print("Rata-rata di bawah atau sama dengan 50")

#3. MENGHITUNG BILANGAN JUMLAH BILANGAN GENAP DAN JUMLAH BILANGAN GANJIL YANG DIMASUKKAN 
N = int(input("Masukkan N: "))

jumlah_genap = 0
jumlah_ganjil = 0

for i in range(N):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    
    if angka % 2 == 0:
        jumlah_genap += 1  
    else:
        jumlah_ganjil += 1  

if jumlah_genap > 0:
    print(f"Jumlah bilangan genap: {jumlah_genap}")
else:
    print("Tidak ada bilangan genap.")

if jumlah_ganjil > 0:
    print(f"Jumlah bilangan ganjil: {jumlah_ganjil}")
else:
    print("Tidak ada bilangan ganjil.")