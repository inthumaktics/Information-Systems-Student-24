#PRAKTIKUM 9 :
#PEMANGGILAN MODUL LUAS
print("Erika")

import luas

luas_segitiga = luas.segitiga(16, 4)
luas_persegi = luas.persegi(5, 6)
luas_lingkaran = luas.lingkaran(25)

print(luas_segitiga)
print(luas_persegi)
print(luas_lingkaran)

#PEMANGGILAN MODUL PERHITUNGAN
import Perhitungan as hitung

hitung.penjumlahan(10, 10)
hitung.Pengurangan(30, 10)
hitung.Perkalian(10, 2)
hitung.Pembagian(20, 2)

#PEMANGGILAN MODUL KALKULATOR BMI
from KalkulatorBMI import Hitung_BMI

Hitung_BMI(60, 150)
