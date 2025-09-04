#---------------FUNCTION----------------------------

#SYNTAX : 
# def functionname(parameters) :
#     "function_docstring"
#     function_suite 
#     return [expression]

#1. Menghitung Luas Segitiga : 
def contohLsegitiga(a, t):
    "Fungsi ini untuk mencari luas segitiga dengan diketahui alas dan tinggi"
    Luas = a * t / 2;
    return Luas 

#2. Mengambil string sebagai input dan perintah mencetaknya : 
def printme(str) :
    "This prints a passed string into this function"
    print(str)
    return

#3. MENGHITUNG LUAS PERSEGI PANJANG : 
def LuasPP(p, l): 
    "Menghitung luas persegi panjang"
    L = p * l
    print(L)
    return 

p = int(input("Masukkan panjang : "))
l = int(input("Masukkan lebar : "))
Luas = p * l
print("Luas :", Luas)

A = LuasPP(4, 3)
S = 2*A
print(S)

#4. KONVERSI SUHU :
#Kode tanpa function : 
print('Pilihan menu ')
print('1. Konversi C ke F')
print('2. Konversi F ke C')
pilih = int(input('Masukkan pilihan menu (1 atau 2) :'))
if pilih == 1 : 
    C = float(input('Masukkan suhu dalam celcius :'))
    F = (C * 9/5) + 32
    print ('Suhu dalam fahrenheit :', F)
elif pilih == 2 :
    F = float(input('Masukkan suhu dalam fahrenheit :'))
    C = (F - 32) * 5/9
    print ('Suhu dalam celcius :', C)
else : 
    print ('Pilihan tidak ada')

#Kode menggunakan function : 
#Konversi C ke F : 
def C2F(C):
    F = (C*9/5)+32
    return F

#Konversi F ke C : 
def F2C(F):
    C = (F-32)*5/9
    return C

#Mengambil input dari user :
def konversi_suhu(suhu, option): 
    "CF. Konversi C ke F"
    "FC. Konversi F ke C"
    if option == 'CF':
        F = C2F(suhu)
        print('Suhu Fahrenheit :', F)
    elif option == 'FC':
        C = F2C(suhu)
        print('Suhu Celcius :', C)
    else :
        print('Pilihan tidak ada')