#MODUL KALKULATOR BMI

def Hitung_BMI(berat, tinggi_cm):
    tinggi_m = tinggi_cm/100
    BMI = berat/(tinggi_m*2)

    if BMI < 18.5:
        print(f"Berat Badan : {berat}")
        print(f"Tinggi Badan : {tinggi_cm}")       
        print("Hasil : Kurang berat badan")
    elif BMI >= 18.5 and BMI < 24.9:
        print("Hasil : Normal")
    elif BMI >= 25 and BMI < 29.9:
        print("Hasil : Kelebihan berat badan")
    elif BMI >= 30 :
        print("Hasil : Obesitas")

