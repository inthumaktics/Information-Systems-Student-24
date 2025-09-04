'''TUGAS 2 PERTEMUAN 2'''

'''Kasus - 1'''
'''Kasus - 2'''


'''Kasus - 3'''

print(''' Kode Baju : 
1. IMP 
2. Prada
3. Gucci
4. Louis Vuitton
5. Kick Denim 
''')

pilih_baju = input("Masukkan kode baju (1-5): ")
ukuran = input("Masukkan Ukuran Baju (S, M, L): ")

if pilih_baju == '1':
    print("IMP")
    if ukuran == 'S':
        print("Harga : 200.000")
    elif ukuran == 'M':
        print("Harga : 220.000")
    else : 
        print("Harga : 250.000 ")

elif pilih_baju == '2':
    print("Prada")
    if ukuran == 'S':
        print("Harga : 150.000")
    elif ukuran == 'M':
        print("Harga : 160.000")
    else :
        print("Harga : 170.000")

elif pilih_baju == '3':
    print("Gucci")
    if ukuran == 'S':
        print("Harga : 200.000")
    elif  ukuran == 'M':
        print("Harga : 200.000")
    else :
        print("Harga : 200.000")

elif pilih_baju == '4':
    print("Louis Vuitton")
    if ukuran == 'S':
        print("Harga : 300.000")
    elif ukuran == 'M':
        print("Harga : 300.000")
    else :  
        print("Harga : 350.000")

elif pilih_baju == '5':
    print("Kick Denim")
    if ukuran == 'S':
        print("Harga : 100.000")
    elif ukuran == 'M':
        print("Harga : 120.000")
    else :
        print("Harga : 130.000")

else : 
    print("Kode baju salah, silakan ulangi lagi!")