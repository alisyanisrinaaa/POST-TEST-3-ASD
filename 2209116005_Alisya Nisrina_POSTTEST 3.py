import os
os.system("cls")

# POST TEST 3 ASD
# Nama : Alisya Nisrina Sativa
# NIM  : 2209116005
# SISTEM INFORMASI A 2022

class App:
    def __init__(self, nama, kategori):
        self.name = nama
        self.kategori = kategori
        self.next = None

class Playstore:
    def __init__(self):
        self.head = None
        self.history = []

    def tambah_app(self):
        nama_app = input("Masukkan Nama Aplikasi : ")
        kategori = input("Masukkan Kategori Aplikasi : ")
        new_app = App(nama_app, kategori)
        if self.head is None:
            self.head = new_app
        else:
            app_baru = self.head
            while app_baru.next is not None:
                app_baru = app_baru.next
            app_baru.next = new_app
        print("")
        print("Yeay! Aplikasi telah berhasil diinstall ^^ ")
        self.history.append(f"Aplikasi Baru : {nama_app} ")

    def hapus_app(self):
        nama_app = input("Masukkan nama aplikasi yang ingin diuninstall : ")
        if self.head is None:
            print("")
            print("Aplikasi belum terinstall")
            print("")
        elif self.head.name == nama_app:
            self.head = self.head.next
            print("")
            print("Aplikasi telah teruninstall")
            print("")
        else:
            app_baru = self.head
            while app_baru.next is not None:
                if app_baru.next.name == nama_app:
                    app_baru.next = app_baru.next.next
                    print("")
                    print("Aplikasi telah teruninstall")
                    print("")
                    return
                app_baru = app_baru.next
            print("")
            print("Aplikasi belum terinstall ")
            print("")
        self.history.append(f"Aplikasi yang baru saja di uninstall : {nama_app} ")

    def lihat_app(self):
        if self.head is None:
            print("")
            print("Tidak ada aplikasi yang terinstall ")
            print("")
        else:
            app_baru = self.head
            while app_baru is not None:
                print("Nama Aplikasi : ", app_baru.name)
                print("Kategori Aplikasi : ", app_baru.kategori)
                print("")
                app_baru = app_baru.next

    def lihat_history(self):
        print("")
        print("History : ")
        print("")
        for a in self.history:
            print(a)

def main():
    appstore = Playstore()
    user = input("Masukkan Nama Anda : ")
    print("")
    print(f" Halo {user}, Selamat Datang ^_^ ".center(45,"-"))
    print("")
    while True:
        print("="*45)
        print(" PLAYSTORE ".center(45,"="))
        print("="*45)
        print("\t1. Download Aplikasi")
        print("\t2. Hapus Aplikasi")
        print("\t3. Tampilkan Aplikasi")
        print("\t4. Lihat History")
        print("\t5. Exit")
        print("="*45)
        pilih = int(input(f"Halo {user}, ingin ke menu apa? "))
        print("")

        if pilih == 1:
            appstore.tambah_app()
            print("")
        elif pilih == 2:
            appstore.hapus_app()
            print("")
        elif pilih == 3:
            appstore.lihat_app()
            print("")
        elif pilih == 4:
            appstore.lihat_history()
            print("")
        elif pilih == 5:
            print(" Terima Kasih ^___^ ".center(45,"-"))
            print("")
            break
        else:
            print("")
            print("Invalid")
            raise SystemExit

if __name__ == "__main__":
    main()