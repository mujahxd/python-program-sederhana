def validasi_id(id_agen):
    if len(id_agen) != 8:
        return False

    if not id_agen.isalnum() or not id_agen.isupper():
        return False

    if id_agen[0].isdigit():
        return False

    huruf = sum(1 for c in id_agen if c.isalpha())
    angka = sum(1 for c in id_agen if c.isdigit())

    if huruf <= angka:
        return False

    return True


def deteksi_agen():
    print("== Sistem Deteksi Agen Rahasia ==")
    id_agen = input("Masukkan ID agen: ").strip()

    if validasi_id(id_agen):
        print(f"ID {id_agen} valid! Agen terverifikasi.")
    else:
        print(f"ID {id_agen} palsu! Agen tidak terdaftar.")


def main():
    while True:
        deteksi_agen()
        lanjut = input("\nPeriksa ID lain (y/n): ").lower()

        if lanjut != "y":
            print("Sistem ditutup. Tetap waspada, agen!")
            break


main()
