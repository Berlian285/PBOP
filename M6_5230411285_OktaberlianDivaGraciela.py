class Order:
    _last_id = 0  

    def __init__(self, name, customer_name, jumlah):
        Order._last_id += 1  
        self._ID = Order._last_id  
        self.name = name
        self.customer_name = customer_name
        self.jumlah = jumlah  

    def set_order(self):
        print(f"Order set with ID: {self._ID}, Name: {self.name}, Customer Name: {self.customer_name}, Jumlah: {self.jumlah}")

    def update_jumlah(self, amount):
        self.jumlah += amount
        print(f"Jumlah untuk Order ID {self._ID} diperbarui. Jumlah baru: {self.jumlah}")


class Delivery:
    def __init__(self, id, name, date, time, address):
        self._id = id  
        self.name = name
        self.date = date
        self.time = time
        self.address = address

    def process_delivery(self):
        print(f"Processing delivery for {self.name} on {self.date} at {self.time} to {self.address}")

    def update_address(self, new_address):
        self.address = new_address
        print(f"Address updated to: {self.address}")


def main_menu():
    orders = []
    deliveries = []

    while True:
        print("\n=== TOKO DIAMOND ===")
        print("1. Buat Order Baru")
        print("2. Perbarui Data")
        print("3. Tampilkan Data")
        print("0. Keluar")

        choice = input("Pilih opsi: ")

        try:
            if choice == '1':
                customer_name = input("Masukkan Nama Pemesan: ")
                name = input("Masukkan Nama Order: ")
                jumlah = int(input("Masukkan Jumlah Order (angka): "))
                order = Order(name, customer_name, jumlah)  
                orders.append(order)
                print(f"Order berhasil dibuat dengan ID otomatis: {order._ID}")

                delivery_choice = input("Apakah Anda ingin membuat Delivery untuk order ini? (ya/tidak): ").strip().lower()
                if delivery_choice == 'ya':
                    date = input("Masukkan Tanggal Delivery (YYYY-MM-DD): ")
                    time = input("Masukkan Jam Delivery (HH:MM): ")
                    address = input("Masukkan Alamat Delivery: ")
                    delivery = Delivery(order._ID, order.name, date, time, address)
                    deliveries.append(delivery)
                    print("Delivery berhasil dibuat.")
                else:
                    print("Delivery tidak dibuat.")

            elif choice == '2':
                print("\n=== Menu Perbarui Data ===")
                print("1. Tambah Order")
                print("2. Hapus Order")
                sub_choice = input("Pilih opsi: ")

                if sub_choice == '1':
                    print("\n=== Tambah Order ===")
                    print("1. Tambah Order Baru dari ID yang tersedia")
                    print("2. Tambah Jumlah Order dari Order dengan ID tertentu")
                    add_choice = input("Pilih opsi: ")

                    if add_choice == '1':
                        order_id = int(input("Masukkan ID Order yang ingin ditambahkan: "))
                        name = input("Masukkan Nama Order Baru: ")
                        customer_name = input("Masukkan Nama Pemesan: ")
                        jumlah = int(input("Masukkan Jumlah Order (angka): "))
                        order = Order(name, customer_name, jumlah)
                        orders.append(order)
                        print(f"Order baru berhasil ditambahkan dengan ID {order._ID}")

                    elif add_choice == '2':
                        order_id = int(input("Masukkan ID Order yang ingin ditambah jumlahnya: "))
                        found = False
                        for order in orders:
                            if order._ID == order_id:
                                found = True
                                amount = int(input("Masukkan jumlah untuk menambah order: "))
                                order.update_jumlah(amount)
                                break
                        if not found:
                            print("Order dengan ID tersebut tidak ditemukan.")

                elif sub_choice == '2':
                    print("\n=== Hapus Order ===")
                    print("1. Hapus Seluruh Order")
                    print("2. Hapus Nama Order berdasarkan ID")
                    print("3. Perbarui Jumlah Order berdasarkan ID")
                    delete_choice = input("Pilih opsi: ")

                    if delete_choice == '1':
                        order_id = int(input("Masukkan ID Order yang ingin dihapus: "))
                        orders = [order for order in orders if order._ID != order_id]
                        print(f"Order dengan ID {order_id} telah dihapus.")

                    elif delete_choice == '2':
                        order_id = int(input("Masukkan ID Order untuk menghapus nama: "))
                        for order in orders:
                            if order._ID == order_id:
                                order.name = ""
                                print(f"Nama Order dengan ID {order_id} telah dihapus.")
                                break

                    elif delete_choice == '3':
                        order_id = int(input("Masukkan ID Order yang ingin diperbarui jumlahnya: "))
                        for order in orders:
                            if order._ID == order_id:
                                new_jumlah = int(input("Masukkan jumlah baru untuk order: "))
                                order.jumlah = new_jumlah
                                print(f"Jumlah Order dengan ID {order_id} diperbarui menjadi {new_jumlah}.")
                                break

            elif choice == '3':
                print("\n=== Menu Tampilkan Data ===")
                print("1. Tampilkan Seluruh Order")
                print("2. Tampilkan Order Berdasarkan ID")
                print("3. Tampilkan Seluruh Delivery yang Sedang di Proses")
                view_choice = input("Pilih opsi: ")

                if view_choice == '1':
                    print("\n=== Daftar Order ===")
                    for order in orders:
                        order.set_order()

                elif view_choice == '2':
                    order_id = int(input("Masukkan ID Order yang ingin ditampilkan: "))
                    found = False
                    for order in orders:
                        if order._ID == order_id:
                            order.set_order()
                            found = True
                            break
                    if not found:
                        print("Order dengan ID tersebut tidak ditemukan.")

                elif view_choice == '3':
                    print("\n=== Daftar Delivery yang Sedang Diproses ===")
                    for delivery in deliveries:
                        delivery.process_delivery()

            elif choice == '0':
                print("Keluar dari program.")
                break

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

        except ValueError:
            print("Input tidak valid! Pastikan memasukkan angka untuk ID atau jumlah order.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

main_menu()
