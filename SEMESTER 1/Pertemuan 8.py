# Print kosong
kosong = []
print(kosong)

prodi = ['SI']
print(prodi)

prodi = ['SI', 'Matematika', 'Fisika', 'Biologi']
print(prodi)

mahasiswa = ['SI', 129, True, 3.4]
print(mahasiswa)

#MENGAMBIL NILAI
buah = ['apel', 'anggur', 'mangga', 'jeruk']
print(buah[2]) #mengambil mangga, maka indeknya 2

# MENGUBAH NILAI 
buah = ['apel', 'anggur', 'mangga', 'jeruk']
buah[2] = 'kelapa' #mengubah nilai indeks ke - 2
print(buah)

#1. PREPEND() : menambah item dari depan

buah = ['apel', 'anggur', 'mangga', 'jeruk']
buah = ['duren']+buah
print(buah)

#2. APPEND() : menambah item dari belakang
buah = ['apel', 'anggur', 'mangga', 'jeruk']
buah = buah+['duren']
print(buah)

#3. INSERT() : menambah item pada indeks tertentu

buah = ['apel', 'anggur', 'mangga', 'jeruk']
buah.insert(2, 'manggis')
print(buah)

#MENGHAPUS ITEM LIST

todo_list = [
    'Belajar Python',
    'Belajar Django',
    'Belajar MongoDB',
    'Belajar Sulap',
    'Belajar Flask'
]
del todo_list[3]
print(todo_list)

#REMOVE()

a = ['a', 'b', 'c', 'd']

a.remove('b')
print(a)

#MEMOTONG LIST

warna = ['merah', 'hijau', 'kuning', 'biru', 'pink', 'ungu']
print(warna[1:5])