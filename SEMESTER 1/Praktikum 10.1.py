### STUDI CASE 1 : TICKET BOOKING
print(60*"="+"TICKET BOOKING"+"="*60)

#1. Data awal kereta :
data_kereta = [
     {"ID" : 1, "Name" : "Express A", "From" : "City X", "To" : "City Y", "Seats" : 50, "Price" : 150},
     {"ID" : 2, "Name" : "Express B", "From" : "City Y", "To" : "City Z", "Seats" : 30, "Price" : 200},
     {"ID" : 3, "Name" : "Express C", "From" : "City X", "To" : "City Z", "Seats" : 20, "Price" : 250},
     {"ID" : 4, "Name" : "Express D", "From" : "City Y", "To" : "City Z", "Seats" : 0,  "Price" : 300},
]

#2. Data tiket yang telah dipesan :
tiket_dipesan = []

while True:
    print("Menu :")
    print("1. Tampilkan daftar kereta")
    print("2. Pesan tiket kereta")
    print("3. Lihat tiket yang sudah dipesan")
    print("4. Keluar")

    pilihan_input = input("Enter Your Choice :")

    if pilihan_input == "1" :
        print("Daftar Kereta :")
        for daftar_kereta in data_kereta:
            print(f"ID Kereta : {daftar_kereta["ID"]}, Name : {daftar_kereta["Name"]}, From : {daftar_kereta["From"]}, To : {daftar_kereta["To"]}, Seats : {daftar_kereta["Seats"]}, Price : {daftar_kereta["Price"]}")
    elif pilihan_input == "2" :
        ID_kereta = int(input("Enter Train ID :"))
        nama_penumpang = input("Enter Passenger Name :")

        kereta_ditemukan = None
        for i in range(len(data_kereta)):
            if data_kereta[i]["ID"] == ID_kereta:
                kereta_ditemukan = i
                break

        if kereta_ditemukan is not None :
            if data_kereta[kereta_ditemukan]["Seats"] > 0:
                data_kereta[kereta_ditemukan]["Seats"] -= 1
                tiket_baru = {"ID_kereta": ID_kereta, "nama_penumpang": nama_penumpang, "nama_kereta": data_kereta[kereta_ditemukan]['Name'], "Price": data_kereta[kereta_ditemukan]['Price']}
                tiket_dipesan.append(tiket_baru)
                print("Ticket booked successfully!")
            else:
                print("Not seats  available on this train") 
        else:
            print("ID kereta tidak ditemukan.")
    elif pilihan_input == '3':
        print("Daftar Tiket yang Sudah Dipesan:")
        for tiket in tiket_dipesan:
            print(f"Passenger: {tiket['nama_penumpang']}, Train: {tiket['nama_kereta']}, Price: {tiket['Price']}")
    elif pilihan_input == '4':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Pilihan tidak valid.")

print(40*"="+"Terima kasih telah mengunjungi program ini, sampai jumpa kembali"+"="*40)

