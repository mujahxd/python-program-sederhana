belanja = ["beras", "gula", "teh"]

while True:
    print("\nDaftar belanja:", belanja)
    print("1. Tambah barang")
    print("2. Hapus barang")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        barang = input("Masukkan nama barang: ")
        belanja.append(barang)
    elif pilihan == "2":
        barang = input("Barang yang mau dihapus: ")
        if barang in belanja:
            belanja.remove(barang)
        else:
            print("Barang tidak ditemukan!")
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid.")
