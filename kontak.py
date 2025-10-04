kontak = {}


def tampilkan_menu():
    print("\nMenu:")
    print("1. Tambah kontak")
    print("2. Lihat semua kontak")
    print("3. Keluar")


while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        nama = input("Masukkan nama kontak: ")
        nomor = input("Masukkan nomor telepon: ")
        kontak[nama] = nomor
        print(f"Kontak '{nama}' ditambahkan.")

    elif pilihan == "2":
        if kontak:
            print("\nDaftar Kontak:")
            for nama, nomor in kontak.items():
                print(f"{nama}: {nomor}")
        else:
            print("Belum ada kontak.")

    elif pilihan == "3":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-3.")
