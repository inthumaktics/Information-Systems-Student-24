# PROGRAM PERULANGAN BERSARANG MENCARI PASANGAN ANGKÀ (X,y)
print('=========PERULANGAN BERSARANG PASANGAN ANGKA (X,Y)===========')

for x in range(1,6) :
    for y in range(1,6):
        if x * y <= 12 :
            print(f'({x}, {y})', end = ' ')
    print()

# PROGRAM MEMERIKSA APAKAH ANGKA X MERUPAKAN KELIPATAN DARI ANGKA Y
print('==========MEMERIKSA ANGKA X KELIPATAN DARI ANGKA Y==========')

x = int(input('Masukkan Angka x = '))
y = int(input('Masukkan Angka y = '))

if x % y == 0:
    print(f'{x} adalah kelipatan dari {y}')
    print('Kelipatan dari ', y, 'hingga', x, '=')
    for i in range(y, x+1, y) :
        print(i, end=' ')