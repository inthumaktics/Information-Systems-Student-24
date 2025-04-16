print("=====1. Mencari Elemen dalam Array=====")

list_array = [10, 20, 30, 40, 50]
target_angka = 30

for i in range(len(list_array)) :
    if list_array[i] == target_angka :
        print("Elemen", target_angka, "ditemukan pada indeks", i)
        break
else :
    print("Elemen", target_angka, "tidak ditemukan")

print("=====2. Reverse Array=====")

### menggunakan perulangan :
list_angka = [1, 2, 3, 4, 5]
list_reverse = []
for i in range(len(list_angka) -1, -1, -1) :
    list_reverse.append(list_angka[i])
print("Hasil menggunakan perulangan = ", list_reverse)

### menggunakan metode reverse :
list_angka = [1, 2, 3, 4, 5]
list_angka.reverse()
print("Hasil metode reverse = ", list_angka)

print("=====3. Sortir Array=====")

list_array = [5, 3, 8, 6, 2]
e = len(list_array)

for i in range(e):
    for j in range(0, e-i-1):
        if list_array[j] > list_array[j+1]:
           list_array[j], list_array[j+1] = list_array[j+1], list_array[j]
print("Sortir Arraynya adalah = ", list_array)

###----------------------------------------------------------------------------------###

### bubble sort
def bubble_sort(list_array):
    n = len(list_array)
    for i in range(n):
        for j in range(0, n-i-1):
            if list_array[j] > list_array[j+1] :
                list_array[j], list_array[j+1] = list_array[j+1], list_array[j]

list_array = [5, 3, 8, 6, 2]
bubble_sort(list_array)
print("Sortir Arraynya adalah = ", list_array, "Ini hasil dari bubble sort")

print("=====4. Program Pencarian Duplikat dalam Array=====")

### menggunakan perulangan bersarang :
list_array = [1, 2, 3, 4, 5, 2, 3]
duplikat = []

for i in range(len(list_array)):
    for j in range(i+1, len(list_array)):
        if list_array[i] == list_array[j]:
            duplikat.append(list_array[i])
            break
print("Elemen Duplikat = ", duplikat, "Ini hasil menggunakan perulangan bersarang")

### menggunakan set :
def find_duplicates_set(arr):
    return list(set([x for x in arr if arr.count(x) > 1]))

list_array = [1, 2, 3, 4, 5, 2, 3]
duplikat = find_duplicates_set(list_array)
print("Elemen Duplikat = ", duplikat, "Ini hasil menggunakan set")

print("=====5. Array dengan String=====")

input_nama = ["Alice", "Bob", "Charlie", "Diana"]
nama_panjang = []

for name in input_nama:
    if len(name) > 4:
        nama_panjang.append(name)

print("Nama dengan panjang lebih dari 4 karakter:", ", ".join(nama_panjang))

