import os

def rupiah(uang):
    return f"Rp. {uang:,.0f}".replace(",", ".")

class DaftarMenu:
    def __init__(self):
        self.makanan = {
            "1. Nasi Goreng": 15000,
            "2. Mie Goreng": 12000,
            "3. Sate Ayam": 25000,
            "4. Ayam Bakar": 22000,
            "5. Bakso": 10000
        }
        self.minuman = {
            "1. Es Teh Manis": 3000,
            "2. Es Jeruk": 4000,
            "3. Jus Alpukat": 7000,
            "4. Kopi": 5000,
            "5. Milkshake": 10000
        }
        self.pilihan = []  

    def lihat_makanan(self):
        print("-------- DAFTAR MAKANAN --------")
        for makanan, harga in self.makanan.items():
            print(f"{makanan} -> {rupiah(harga)}")
    
    def lihat_minuman(self):
        print("-------- DAFTAR MINUMAN --------")
        for minuman, harga in self.minuman.items():
            print(f"{minuman} -> {rupiah(harga)}")

    def pilih_menu(self):
        try:
            print("---------- PILIH MENU ----------")
            print("1. Tambah Makanan")
            print("1. Tambah Minuman")
            tambah = input("Masukkan Pilihan 1 atau 2: ")
            if tambah not in ['1', '2']:
                raise ValueError("Kategori harus 1 atau 2.")
            
            if tambah == '1':
                self.lihat_makanan()
                pilihan = input("Masukkan nomor makanan yang dipilih: ")
                for makanan, harga in self.makanan.items():
                    if makanan.startswith(pilihan + "."):
                        self.pilihan.append((makanan, harga))
                        print(f"{makanan} telah ditambahkan ke pilihan.")
                        break
                else:
                    print("Nomor makanan tidak ditemukan.")
            
            elif tambah == '2':
                self.lihat_minuman()
                pilihan = input("Masukkan nomor minuman yang dipilih: ")
                for minuman, harga in self.minuman.items():
                    if minuman.startswith(pilihan + "."):
                        self.pilihan.append((minuman, harga))
                        print(f"{minuman} telah ditambahkan ke pilihan.")
                        break
                else:
                    print("Nomor minuman tidak ditemukan.")
        except ValueError as e:
            print(f"Input tidak valid: {e}")

    def lihat_pilihan(self):
        if not self.pilihan:
            print("Anda belum memilih menu apa pun.")
        else:
            print("-------- MENU YANG DIPILIH --------")
            total = 0
            for item, harga in self.pilihan:
                print(f"{item} -> {rupiah(harga)}")
                total += harga
            print(f"Total: {rupiah(total)}")

def main():
    menu = DaftarMenu()
    while True:
        print("======== PILIHAN MENU ========")
        print("1. Lihat Daftar Makanan")
        print("2. Lihat Daftar Minuman")
        print("3. Pilih Menu")
        print("4. Lihat Daftar Menu yang Dipilih")
        print("0. Keluar")
        
        try:
            pilihan = input("Masukkan Pilihan: ")
            if pilihan not in ['1', '2', '3', '4', '0']:
                raise ValueError("Pilihan harus antara 0 hingga 4.")
            
            if pilihan == '1':
                menu.lihat_makanan()
            elif pilihan == '2':
                menu.lihat_minuman()
            elif pilihan == '3':
                menu.pilih_menu()
            elif pilihan == '4':
                menu.lihat_pilihan()
            elif pilihan == '0':
                print("Terima kasih! Sampai jumpa.")
                break
        except ValueError as e:
            print(f"Input tidak valid: {e}")
        
if __name__ == "__main__":
    main()
