class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat

    def info(self):
        return f"{self.nik:<10} | {self.nama:<20} | {self.alamat:<30}"

class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        self.harga = harga

    def info(self):
        return f"{self.kode_produk:<10} | {self.nama_produk:<20} | {self.jenis_produk:<10} | Rp{self.harga:<10,}"

class Snack(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, "Snack", harga)

class Makanan(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, "Makanan", harga)

class Minuman(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, "Minuman", harga)

class Transaksi:
    def __init__(self, no_transaksi, pegawai, produk_list, pembayaran):
        self.no_transaksi = no_transaksi
        self.pegawai = pegawai
        self.produk_list = produk_list  
        self.pembayaran = pembayaran

    def total_harga(self):
        return sum([produk.harga * jumlah for produk, jumlah in self.produk_list])

    def total_item(self):
        return sum([jumlah for _, jumlah in self.produk_list])

    def kembalian(self):
        return self.pembayaran - self.total_harga()

    def info(self):
        produk_info = "\n".join([f"{produk.info()} | Jumlah: {jumlah}" for produk, jumlah in self.produk_list])
        return (f"No Transaksi: {self.no_transaksi}\nPegawai: {self.pegawai.info()}\nProduk:\n{produk_info}\n"
                f"Total Item: {self.total_item()}\nTotal Harga: Rp{self.total_harga():,}\n"
                f"Pembayaran: Rp{self.pembayaran:,}\nKembalian: Rp{self.kembalian():,}")

class Struk:
    def __init__(self, transaksi):
        self.transaksi = transaksi

    def print_struk(self):
        print("\n=== STRUK PEMBELIAN ===")
        print(self.transaksi.info())
        print("=======================\n")

def main_menu():
    pegawai_list = {
        "123": Pegawai("123", "Berlian", "Mandala")
    }
    
    produk_list = [
        Snack("S001", "Chips", 5000),
        Snack("S002", "Popcorn", 7000),
        Snack("S003", "Pretzel", 6500),
        Snack("S004", "Cookies", 8000),
        Snack("S005", "Candy", 3000),
        
        Makanan("M001", "Nasi Goreng", 15000),
        Makanan("M002", "Mie Goreng", 12000),
        Makanan("M003", "Ayam Bakar", 20000),
        Makanan("M004", "Sate", 18000),
        Makanan("M005", "Bakso", 13000),
        
        Minuman("D001", "Es Teh", 5000),
        Minuman("D002", "Kopi", 10000),
        Minuman("D003", "Soda", 7000),
        Minuman("D004", "Jus Mangga", 12000),
        Minuman("D005", "Air Mineral", 3000)
    ]
    transaksi_counter = 1  

    while True:
        print("\n=== Menu Utama ===")
        print("1. Tambah data pegawai")
        print("2. Lihat data pegawai")
        print("3. Lihat daftar produk")
        print("4. Buat transaksi")
        print("5. Keluar")
        
        choice = input("Pilih menu: ")
        
        if choice == '1':
            nik = input("Masukkan NIK Pegawai: ")
            nama = input("Masukkan Nama Pegawai: ")
            alamat = input("Masukkan Alamat Pegawai: ")
            pegawai = Pegawai(nik, nama, alamat)
            pegawai_list[nik] = pegawai
            print("Data pegawai berhasil ditambahkan.")
        
        elif choice == '2':
            if pegawai_list:
                print("\nDaftar Pegawai:")
                print("NIK       | Nama                 | Alamat                        ")
                print("==========|======================|===============================")
                for nik, pegawai in pegawai_list.items():
                    print(pegawai.info())
            else:
                print("Belum ada data pegawai.")
        
        elif choice == '3':
            print("\n=== Daftar Produk ===")
            
            print("\n--- Snack ---")
            print("Kode Produk | Nama Produk         | Jenis      | Harga      ")
            print("============|=====================|============|============")
            for produk in produk_list:
                if produk.jenis_produk == "Snack":
                    print(produk.info())
                    
            print("\n--- Makanan ---")
            print("Kode Produk | Nama Produk         | Jenis      | Harga      ")
            print("============|=====================|============|============")
            for produk in produk_list:
                if produk.jenis_produk == "Makanan":
                    print(produk.info())
                    
            print("\n--- Minuman ---")
            print("Kode Produk | Nama Produk         | Jenis      | Harga      ")
            print("============|=====================|============|============")
            for produk in produk_list:
                if produk.jenis_produk == "Minuman":
                    print(produk.info())
        
        elif choice == '4':
            nik = input("Masukkan NIK Pegawai yang melayani: ")
            pegawai = pegawai_list.get(nik)
            if not pegawai:
                print("Pegawai tidak ditemukan.")
                continue

            print("\nDaftar Produk yang Tersedia:")
            for idx, produk in enumerate(produk_list, 1):
                print(f"{idx}. {produk.info()}")
            
            produk_terpilih = []
            while True:
                pilih_produk = input("Pilih nomor produk (atau ketik 'selesai' jika sudah selesai memilih): ")
                if pilih_produk.lower() == 'selesai':
                    break
                try:
                    index = int(pilih_produk) - 1
                    if 0 <= index < len(produk_list):
                        jumlah = int(input(f"Masukkan jumlah untuk {produk_list[index].nama_produk}: "))
                        produk_terpilih.append((produk_list[index], jumlah))
                        print(f"{produk_list[index].nama_produk} (jumlah: {jumlah}) ditambahkan.")
                    else:
                        print("Nomor produk tidak valid.")
                except ValueError:
                    print("Masukkan nomor produk yang valid.")

            if not produk_terpilih:
                print("Tidak ada produk yang dipilih.")
                continue

            transaksi_total = sum([produk.harga * jumlah for produk, jumlah in produk_terpilih])
            print(f"\nTotal Harga: Rp{transaksi_total:,}")
            pembayaran = int(input("Masukkan jumlah pembayaran: Rp"))
            
            no_transaksi = f"T{transaksi_counter:03}"
            transaksi = Transaksi(no_transaksi, pegawai, produk_terpilih, pembayaran)
            transaksi_counter += 1
            
            if transaksi.kembalian() < 0:
                print("Uang tidak cukup untuk transaksi.")
            else:
                struk = Struk(transaksi)
                struk.print_struk()
        
        elif choice == '5':
            print("Terima kasih! Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main_menu()
