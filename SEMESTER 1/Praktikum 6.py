print('==========PROGRAM LOGIN PENGGUNA TERDAFTAR==========')

usename_terdaftar = 'user123'
password_terdaftar = 'pass123'

while True:
    username_login = input('Masukkan username :')
    password_login = input('Masukkan password :')

    if username_login == 'user123' and password_login == 'pass123':
        print('Login berhasil!')
        break
    else:
        print('Username atau password salah. Coba lagi.')

print('==========SELAMAT ANDA BERHASIL LOGIN KE HALAMAN INI=========')

print('----------------------------------------------------------------')

print('==========PROGRAM MENCARI BILANGAN PRIMA==========')

angka = int(input('Masukkan angka anda :'))
pembagi = 2
is_prima = True

while pembagi < angka :
    if angka % pembagi == 0:
        is_prima = False
        break
    pembagi +=1
if is_prima :
    print('angka', angka, 'adalah bilangan prima')
else:
    print('angka', angka, 'bukan bilangan prima')

print('===========TERIMA KASIH TELAH MENCOBA PROGRAM INI==========')