kamus = {
    "cat": "kucing",
    "dog": "anjing",
    "book": "buku"
}


def tambah_kata():
    kata = input("Masukkan kata (english): ").lower()
    if kata in kamus:
        print("kata sudah ada di kamus.")
    else:
        arti = input("Masukkan terjemahan (indonesia): ").lower()
        kamus[kata] = arti
        print(f"Kata '{kata}' berhasil ditambahkan.")


def cari_kata():
    kata = input("Masukkan kata yang ingin dicari: ").lower()
    if kata in kamus:
        print(f"{kata} -> {kamus[kata]}")
    else:
        print(f"Kata '{kata}' tidak ditemukan di kamus.")


while True:
    print("\n=== Kamus Sederhana ===")
    print("1. Tambah kata baru")
    print("2. Cari kata")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        tambah_kata()
    elif pilihan == '2':
        cari_kata()
    elif pilihan == '3':
        print("Terima kasih, program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
