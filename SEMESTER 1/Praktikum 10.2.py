# STUDI CASE 2 : GAME TEBAK ANGKA

print(60*"="+"GAME TEBAK ANGKA"+"="*60)

import random

def tebak_angka():

    print("Selamat datang di permainan Tebak Angka!")
    print("Tebak angka yang telah saya pikirkan.")

    #1. Pilih level yang diinginkan :
    level = int(input("Pilih tingkat kesulitan (1-4): "))
    if level == 1:
        batas_atas = 10
    elif level == 2:
        batas_atas = 15
    elif level == 3:
        batas_atas = 20
    elif level == 4:
        batas_atas = int(input("Masukkan batas atas: "))
    else:
        print("Pilihan level tidak valid.")
        return

    # 2. Acak angka :
    angka_rahasia = random.randint(1, batas_atas)

    kesempatan = 5
    while kesempatan > 0:
        tebakan = int(input("Tebakan Anda: "))
        kesempatan -= 1

        if tebakan == angka_rahasia:
            print("Selamat, Anda benar!")
            break
        elif tebakan < angka_rahasia:
            print("Terlalu rendah.")
        else:
            print("Terlalu tinggi.")

    if kesempatan == 0:
        print(f"Anda kehabisan kesempatan. Angka rahasianya adalah {angka_rahasia}")

    # 3. Pilihan bermain kembali :
    main_lagi = input("Apakah Anda ingin bermain lagi? (yes/no): ").lower()
    if main_lagi == 'yes':
        tebak_angka()

if __name__ == "__main__":
    tebak_angka()

print(40*"="+"Terima kasih telah memainkan game ini, silakan datang kembali"+"="*40)