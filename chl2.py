#Cek Ganjil

while True:
    print("========== Cek Bilangan ==========")
    print("1. Bilangan Prima")
    print("2. Bilangan Ganjil")
    print("3. Bilangan Genap")
    print("0. Keluar")

    pilihan = input("Masukkan Angka Pilihan Menu:")

    if pilihan == '1':
        print("========== Cek Bilangan Prima ==========")
        try:
            bilangan_awal = int(input("Masukkan Bilangan Awal:"))
            bilangan_akhir = int(input("Masukkan Bilangan Akhir:"))
            print(f"Bilangan Prima Dari {bilangan_awal} Sampai {bilangan_akhir}")
            for i in range(bilangan_awal, bilangan_akhir + 1):
                if i > 1:
                    prima=True
                    for j in range (2, int (i ** 0.5)+1):
                        if i % j == 0:
                            prima=False
                            break
                    if prima:
                        print(i, end=" ")
            print()

        except ValueError:
            print("Tidak Valid")

    elif pilihan == '2':
        print("========== Cek Bilangan Ganjil ==========")
        try:
            bilangan_awal = int(input("Masukkan Bilangan Awal:"))
            bilangan_akhir = int(input("Masukkan Bilangan Akhir:"))
            print(f"Bilangan Ganjil Dari {bilangan_awal} Sampai {bilangan_akhir}")
            for i in range(bilangan_awal, bilangan_akhir + 1):
                if i % 2 != 0:
                    print(i, end=" ")
            print()

        except ValueError:
            print("Tidak Valid")

    elif pilihan == '3':
        print("========== Cek Bilangan Genap ==========")
        try:
            bilangan_awal = int(input("Masukkan Bilangan Awal:"))
            bilangan_akhir = int(input("Masukkan Bilangan Akhir:"))
            print(f"Bilangan Genap Dari {bilangan_awal} Sampai {bilangan_akhir}")
            for i in range(bilangan_awal, bilangan_akhir + 1):
                if i % 2 == 0:
                    print(i, end=" ")
                else:
                    "Tidak Valid"
            print()
        
        except ValueError:
            print("Tidak Valid")

    elif pilihan == '0':
        print("Program Selesai, Terima Kasih :)")
        break

    else:
        print("Pilihan Tidak Tersedia di Menu")