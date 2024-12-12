import mysql.connector
try:
    conn = mysql.connector.connect(
        user="root",
        host="localhost",
        password="",
        database="penjualan"
    )
    cur = conn.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)


# # Membuat database 
# cur.execute("CREATE DATABASE IF NOT EXISTS penjualan")
# cur.execute("USE penjualan")

# # Membuat Tabel Pegawai
# cur.execute("""
# CREATE TABLE IF NOT EXISTS Pegawai (
#     NIK CHAR(4) NOT NULL PRIMARY KEY,
#     Nama VARCHAR(50),
#     Alamat VARCHAR(255)
# )
# """)

# # Membuat Tabel Produk dengan kolom Harga
# cur.execute("""
# CREATE TABLE IF NOT EXISTS Produk (
#     Kode_Produk CHAR(4) NOT NULL PRIMARY KEY,
#     Nama_Produk VARCHAR(50),
#     Jenis_Produk VARCHAR(20),
#     Harga INT 
# )
# """)

# # Membuat Tabel Transaksi
# cur.execute("""
# CREATE TABLE IF NOT EXISTS Transaksi (
#     No_Transaksi CHAR(4) NOT NULL PRIMARY KEY,
#     NIK CHAR(4) NOT NULL,
#     Detail_Transaksi VARCHAR(255),
#     FOREIGN KEY (NIK) REFERENCES Pegawai(NIK)
# )
# """)

# # Membuat Tabel Relasi Transaksi dengan Produk
# cur.execute("""
# CREATE TABLE IF NOT EXISTS Transaksi_Produk (
#     No_Transaksi CHAR(4),
#     Kode_Produk CHAR(4),
#     Jumlah_Produk INT,
#     PRIMARY KEY (No_Transaksi, Kode_Produk),
#     FOREIGN KEY (No_Transaksi) REFERENCES Transaksi(No_Transaksi),
#     FOREIGN KEY (Kode_Produk) REFERENCES Produk(Kode_Produk)
# )
# """)

# # Membuat Tabel Struk
# cur.execute("""
# CREATE TABLE IF NOT EXISTS Struk (
#     No_Transaksi CHAR(4) NOT NULL PRIMARY KEY,
#     Nama_Pegawai VARCHAR(50),
#     Total_Harga DECIMAL(10, 2),
#     FOREIGN KEY (No_Transaksi) REFERENCES Transaksi(No_Transaksi)
# )
# """)

# print("Database, tabel, dan relasi telah dibuat sesuai dengan kebutuhan.")




def input_data_pegawai():
    try: 
        nik = input("Masukkan NIK: ")
        nama = input("Masukkan Nama: ")
        alamat = input("Masukkan Alamat: ")
        cur.execute("INSERT INTO Pegawai (NIK, Nama, Alamat) VALUES (%s, %s, %s)", (nik, nama, alamat))
        conn.commit()
        print("Data Pegawai berhasil ditambahkan.")
    except mysql.connector.Error as err:
        print(f"Error saat menambahkan data Pegawai: {err}")

def tampil_data_pegawai():
    try:
        cur.execute("SELECT * FROM Pegawai")
        result = cur.fetchall()
        print("\nData Pegawai:")
        for row in result:
            print(f"NIK: {row[0]}, Nama: {row[1]}, Alamat: {row[2]}")
    except mysql.connector.Error as err:
        print(f"Error saat menampilkan data Pegawai: {err}")

def hapus_data_pegawai():
    try:
        nik = input("Masukkan NIK Pegawai yang akan dihapus: ")
        cur.execute("DELETE FROM Pegawai WHERE NIK = %s", (nik,))
        conn.commit()
        print("Data Pegawai berhasil dihapus.")
    except mysql.connector.Error as err:
        print(f"Error saat menghapus data Pegawai: {err}")

def input_data_produk():
    try:
        kode_produk = input("Masukkan Kode Produk: ")
        nama_produk = input("Masukkan Nama Produk: ")
        jenis_produk = input("Masukkan Jenis Produk: ")
        harga = int(input("Masukkan Harga Produk: "))
        cur.execute("INSERT INTO Produk (Kode_Produk, Nama_Produk, Jenis_Produk, Harga) VALUES (%s, %s, %s, %s)",
                    (kode_produk, nama_produk, jenis_produk, harga))
        conn.commit()
        print("Data Produk berhasil ditambahkan.")
    except ValueError:
        print("Input harga harus berupa angka.")
    except mysql.connector.Error as err:
        print(f"Error saat menambahkan data Produk: {err}")

def tampil_data_produk():
    try:
        cur.execute("SELECT * FROM Produk")
        result = cur.fetchall()
        print("\nData Produk:")
        for row in result:
            print(f"Kode Produk: {row[0]}, Nama: {row[1]}, Jenis: {row[2]}, Harga: Rp. {row[3]:,}")
    except mysql.connector.Error as err:
        print(f"Error saat menampilkan data Produk: {err}")

def hapus_data_produk():
    try:
        kode_produk = input("Masukkan Kode Produk yang akan dihapus: ")
        cur.execute("DELETE FROM Produk WHERE Kode_Produk = %s", (kode_produk,))
        conn.commit()
        print("Data Produk berhasil dihapus.")
    except mysql.connector.Error as err:
        print(f"Error saat menghapus data Produk: {err}")

def input_data_transaksi():
    try:
        no_transaksi = input("Masukkan No Transaksi: ")
        nik_pegawai = input("Masukkan NIK Pegawai: ")

        cur.execute("SELECT * FROM Pegawai WHERE NIK = %s", (nik_pegawai,))
        pegawai = cur.fetchone()

        if pegawai is None:
            print("Error: NIK Pegawai tidak ditemukan.")
            return

        print("\nDaftar Produk yang Tersedia:")
        cur.execute("SELECT * FROM Produk")
        result_produk = cur.fetchall()
        for row in result_produk:
            print(f"Kode Produk: {row[0]}, Nama: {row[1]}, Jenis: {row[2]}, Harga: Rp. {row[3]:,.2f}")

        produk_beli = []
        while True:
            kode_produk = input("Masukkan Kode Produk yang dibeli (atau ketik 'selesai' untuk selesai): ")
            if kode_produk == 'selesai':
                break

            cur.execute("SELECT * FROM Produk WHERE Kode_Produk = %s", (kode_produk,))
            produk = cur.fetchone()

            if produk is None:
                print("Error: Kode Produk tidak ditemukan.")
                continue

            jumlah = int(input(f"Masukkan Jumlah Produk {produk[1]}: "))
            produk_beli.append((kode_produk, jumlah))

        total_harga = 0
        for kode_produk, jumlah in produk_beli:
            cur.execute("SELECT Harga FROM Produk WHERE Kode_Produk = %s", (kode_produk,))
            harga_produk = cur.fetchone()[0]
            total_harga += harga_produk * jumlah

        cur.execute(
            "INSERT INTO Transaksi (No_Transaksi, NIK, Detail_Transaksi) VALUES (%s, %s, %s)",
            (no_transaksi, nik_pegawai, f"Pembelian produk sejumlah {len(produk_beli)} item.")
        )
        
        for kode_produk, jumlah in produk_beli:
            cur.execute(
                "INSERT INTO Transaksi_Produk (No_Transaksi, Kode_Produk, Jumlah_Produk) VALUES (%s, %s, %s)",
                (no_transaksi, kode_produk, jumlah)
            )

        conn.commit()
        print("Data Transaksi dan Produk berhasil ditambahkan.")

    except mysql.connector.Error as err:
        print(f"Error saat menambahkan data Transaksi: {err}")

def tampil_data_transaksi():
    try:
        cur.execute("SELECT * FROM Transaksi")
        result = cur.fetchall()
        print("\nData Transaksi:")
        if result:
            for row in result:
                print(f"No Transaksi: {row[0]}, NIK: {row[1]}, Detail: {row[2]}")
        else:
            print("Tidak ada data transaksi.")
    except mysql.connector.Error as err:
        print(f"Terjadi kesalahan saat mengambil data transaksi: {err}")

def hapus_data_transaksi():
    try:
        no_transaksi = input("Masukkan No Transaksi yang akan dihapus: ")
        cur.execute("DELETE FROM Transaksi WHERE No_Transaksi = %s", (no_transaksi,))
        conn.commit()

        if cur.rowcount > 0:
            print("Data Transaksi berhasil dihapus.")
        else:
            print("No Transaksi tidak ditemukan.")
    except mysql.connector.Error as err:
        print(f"Terjadi kesalahan saat menghapus data transaksi: {err}")

def input_data_struk():
    try:
        no_transaksi = input("Masukkan No Transaksi: ")

        cur.execute("SELECT * FROM transaksi WHERE No_Transaksi = %s", (no_transaksi,))
        transaksi = cur.fetchone()
        
        if transaksi is None:
            print("Transaksi tidak ditemukan.")
            return

        nik_pegawai = transaksi[1]  
        cur.execute("SELECT Nama FROM Pegawai WHERE NIK = %s", (nik_pegawai,))
        pegawai = cur.fetchone()

        if pegawai is None:
            print("Pegawai dengan NIK tersebut tidak ditemukan.")
            return

        nama_pegawai = pegawai[0]  

        cur.execute("""
            SELECT SUM(Produk.Harga * Transaksi_Produk.Jumlah_Produk)
            FROM Transaksi_Produk
            JOIN Produk ON Transaksi_Produk.Kode_Produk = Produk.Kode_Produk
            WHERE Transaksi_Produk.No_Transaksi = %s
        """, (no_transaksi,))

        result = cur.fetchone()
        if result[0] is not None and result[0] > 0:
            total_harga = result[0]
        else:
            print("Tidak ada produk yang dibeli dalam transaksi ini.")
            return

        cur.execute("INSERT INTO Struk (No_Transaksi, Nama_Pegawai, Total_Harga) VALUES (%s, %s, %s)",
                    (no_transaksi, nama_pegawai, total_harga))
        conn.commit()
        print("Data Struk berhasil ditambahkan.")
    
    except mysql.connector.Error as err:
        print(f"Error saat menambahkan data Struk: {err}")

def tampil_data_struk():
    try:
        cur.execute("SELECT * FROM Struk")
        result = cur.fetchall()
        print("\nData Struk:")
        if result:
            for row in result:
                print(f"No Transaksi: {row[0]}, Kode Pegawai: {row[1]}, Total Harga: Rp. {row[2]:,.2f}")
        else:
            print("Tidak ada data struk.")
    except mysql.connector.Error as err:
        print(f"Terjadi kesalahan saat mengambil data struk: {err}")

def hapus_data_struk():
    try:
        no_transaksi = input("Masukkan No Transaksi yang akan dihapus: ")
        cur.execute("DELETE FROM Struk WHERE No_Transaksi = %s", (no_transaksi,))
        conn.commit()

        if cur.rowcount > 0:
            print("Data Struk berhasil dihapus.")
        else:
            print("No Transaksi tidak ditemukan.")
    except mysql.connector.Error as err:
        print(f"Terjadi kesalahan saat menghapus data struk: {err}")



while True:
    print("==========Menu Utama==========")
    print("1. Kelola Pegawai")
    print("2. Kelola Produk")
    print("3. Kelola Transaksi")
    print("4. Kelola Struk")
    print("0. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("==========Kelola Pegawai==========")
        print("1. Input Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        sub_pilihan = input("Pilih submenu: ")
        if sub_pilihan == "1":
            input_data_pegawai()
        elif sub_pilihan == "2":
            tampil_data_pegawai()
        elif sub_pilihan == "3":
            hapus_data_pegawai()

    elif pilihan == "2":
        print("==========Kelola Produk==========")
        print("1. Input Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        sub_pilihan = input("Pilih submenu: ")
        if sub_pilihan == "1":
            input_data_produk()
        elif sub_pilihan == "2":
            tampil_data_produk()
        elif sub_pilihan == "3":
            hapus_data_produk()

    elif pilihan == "3":
        print("==========Kelola Transaksi==========")
        print("1. Input Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        sub_pilihan = input("Pilih submenu: ")
        if sub_pilihan == "1":
            input_data_transaksi()
        elif sub_pilihan == "2":
            tampil_data_transaksi()
        elif sub_pilihan == "3":
            hapus_data_transaksi()

    elif pilihan == "4":
        print("==========Kelola Struk==========")
        print("1. Input Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        sub_pilihan = input("Pilih submenu: ")
        if sub_pilihan == "1":
            input_data_struk()
        elif sub_pilihan == "2":
            tampil_data_struk()
        elif sub_pilihan == "3":
            hapus_data_struk()

    elif pilihan == "0":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")


