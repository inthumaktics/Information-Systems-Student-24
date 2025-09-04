#1. Program menentukan nilai maksimum dari tiga buah bilangan :
x = 3
y = 8
z = 10

if x > y and x > z :
    print(f" Nilai maksimum dari x adalah :{x} ")
elif y > x and y > z :
    print(f" Nilai maksimum dari y adalah :{y} ")
elif z > x and z > y :
    print(f" Nilai maksimum dari z adalah :{z} ")

#2. Program menentukan nilai minimum dari tiga buah bilangan 
x = 3
y = 8
z = 10

if x < y and x < z:
    print(f" Nilai minimum dari x adalah :{x} ")
elif y < x and y < z:
    print(f" Nilai minimum dari y adalah :{y} ")
elif z < x and z < y:
    print(f" Nilai minimum dari z adalah :{z} ")

#3. Program menghitung Body Mass Index (BMI)
berat_badan = int(input("Masukkan berat badan Anda (kg):"))
tinggi_badan = int(input("Masukkan tinggi badan Anda (cm): "))

tinggi_badan = tinggi_badan/100
BMI = berat_badan/(tinggi_badan**2)

if BMI < 18.5:
    print("Hasil : Kurang berat badan")
elif BMI >= 18.5 and BMI < 24.9:
    print("Hasil : Normal")
elif BMI >= 25 and BMI < 29.9:
    print("Hasil : Kelebihan berat badan")
elif BMI >= 30 :
    print("Hasil : Obesitas")