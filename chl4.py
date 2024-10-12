class debitur:
    def __init__(self, nama, ktp, limit_pinjaman):
        self.nama = nama
        self.ktp = ktp
        self.limit_pinjaman = limit_pinjaman


class pinjaman:
    def __init__(self, nama_debitur, jumlah, bunga, bulan):
        self.nama_debitur = nama_debitur
        self.jumlah = jumlah
        self.bunga = bunga
        self.bulan = bulan
        self.angsuran = self.hitung_angsuran()

    def hitung_angsuran(self):
        total_pinjaman = self.jumlah + (self.jumlah * self.bunga / 100)
        return total_pinjaman / self.bulan


class pinjol:
    def __init__(self):
        self.daftar_debitur = []
        self.daftar_pinjaman = []

    # Bagian untuk Kelola Debitur
    def tambah_debitur(self, nama, ktp, limit_pinjaman):
        if any(debitur.ktp == ktp for debitur in self.daftar_debitur):
            print(f"KTP '{ktp}' sudah ada.")
        else:
            debitur_baru = debitur(nama, ktp, limit_pinjaman)
            self.daftar_debitur.append(debitur_baru)
            print(f"Debitur '{nama}' berhasil ditambahkan.")

    def tampilkan_debitur(self):
        if not self.daftar_debitur:
            print("Belum ada debitur yang terdaftar.")
        else:
            print("\n================= Daftar Debitur =================")
            print(f"{'Nama Debitur':<20}{'No KTP':<15}{'Limit Pinjaman':>20}")
            for debitur in self.daftar_debitur:
                print(f"{debitur.nama:<20}{debitur.ktp:<15}Rp.{debitur.limit_pinjaman:>15,}")
        input("\nTekan Enter untuk melanjutkan...")

    def cari_debitur(self, ktp):
        debitur_ditemukan = next((debitur for debitur in self.daftar_debitur if debitur.ktp == ktp), None)
        if debitur_ditemukan:
            print("\n================= Detail Debitur =================")
            print(f"Nama Debitur: {debitur_ditemukan.nama}")
            print(f"No KTP: {debitur_ditemukan.ktp}")
            print(f"Limit Pinjaman: Rp.{debitur_ditemukan.limit_pinjaman:,}")
        else:
            print(f"Debitur dengan KTP '{ktp}' tidak ditemukan.")
        input("\nTekan Enter untuk melanjutkan...")

    def tambah_pinjaman(self, nama_debitur, jumlah, bunga, bulan):
        debitur_ditemukan = next((debitur for debitur in self.daftar_debitur if debitur.nama.lower() == nama_debitur.lower()), None)
        if debitur_ditemukan:
            pinjaman_baru = pinjaman(nama_debitur, jumlah, bunga, bulan)
            self.daftar_pinjaman.append(pinjaman_baru)
            print(f"Pinjaman sebesar Rp.{jumlah:,} untuk '{nama_debitur}' berhasil ditambahkan.")
        else:
            print(f"Debitur '{nama_debitur}' tidak ditemukan.")

    def tampilkan_pinjaman(self):
        if not self.daftar_pinjaman:
            print("Belum ada pinjaman yang terdaftar.")
        else:
            print("\n=================================================== Daftar Pinjaman ===================================================")
            print(f"{'Nama Debitur':<15}{'Jumlah Pinjaman':>25}{'Bunga (%)':>20}{'Bulan':>15}{'Angsuran':>25}")
            for pinjaman in self.daftar_pinjaman:
                print(f"{pinjaman.nama_debitur:<15}Rp.{pinjaman.jumlah:>22,}{pinjaman.bunga:>18.2f}%{pinjaman.bulan:>15}Rp.{pinjaman.angsuran:>23,.2f}")
        input("\nTekan Enter untuk melanjutkan...")

    def menu_kelola_debitur(self):
        while True:
            print("\n================= Kelola Debitur =================")
            print("1. Tampilkan Semua Debitur")
            print("2. Cari Debitur")
            print("3. Tambah Debitur")
            print("0. Kembali")
            pilihan = input("Masukan Pilihan Sub Menu: ")

            if pilihan == '1':
                self.tampilkan_debitur()
            elif pilihan == '2':
                ktp = input("Masukan No KTP Debitur: ")
                self.cari_debitur(ktp)
            elif pilihan == '3':
                nama = input("Masukan Nama Debitur: ")
                ktp = input("Masukan No KTP: ")
                limit_pinjaman = int(input("Masukan Limit Pinjaman (dalam Rupiah): "))
                self.tambah_debitur(nama, ktp, limit_pinjaman)
            elif pilihan == '0':
                break
            else:
                print("Pilihan tidak valid, coba lagi!")

    def menu_pinjaman(self):
        while True:
            print("\n================= Kelola Pinjaman =================")
            print("1. Tambah Pinjaman")
            print("2. Tampilkan Semua Pinjaman")
            print("0. Kembali")
            pilihan = input("Masukan Pilihan Sub Menu: ")

            if pilihan == '1':
                nama_debitur = input("Masukan Nama Debitur: ")
                jumlah = int(input("Masukan Jumlah Pinjaman (dalam Rupiah): "))
                bunga = float(input("Masukan Bunga Pinjaman (dalam %): "))
                bulan = int(input("Masukan Lama Pinjaman (dalam bulan): "))
                self.tambah_pinjaman(nama_debitur, jumlah, bunga, bulan)
            elif pilihan == '2':
                self.tampilkan_pinjaman()
            elif pilihan == '0':
                break
            else:
                print("Pilihan tidak valid, coba lagi!")

    def menu_utama(self):
        while True:
            print("\n================= Admin Pinjol =================")
            print("1. Kelola Debitur")
            print("2. Pinjaman")
            print("0. Keluar")
            pilihan = input("Masukan Pilihan Menu: ")

            if pilihan == '1':
                self.menu_kelola_debitur()
            elif pilihan == '2':
                self.menu_pinjaman()
            elif pilihan == '0':
                print("Keluar dari sistem.")
                break
            else:
                print("Pilihan tidak valid, coba lagi!")


sistem_pinjol = pinjol()

sistem_pinjol.menu_utama()
