#PEMANGGILAN 1
import ModulePerhitungan as hitung

hitung.penjumlahan(20, 10)
hitung.Pengurangan(30, 20)
hitung.Perkalian(45, 7)
hitung.Pembagian(100, 5)

print("="*40)
#PEMANGGILAN 2
from ModulePerhitungan import penjumlahan as t, Pengurangan as k, Perkalian as kl, Pembagian as bg

t(20, 20)
k(100, 10)
kl(50, 5)
bg(70, 3)