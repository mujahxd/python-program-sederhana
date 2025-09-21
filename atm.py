# ATM Sederhana dengan Python

# Data awal
PIN = "1234"
saldo = 1_000_000  # saldo awal

# Input PIN dengan 3x kesempatan
kesempatan = 3
while kesempatan > 0:
    pin_input = input("Masukkan PIN: ")
    if pin_input == PIN:
        print("PIN benar. Selamat datang!\n")
        break
    else:
        kesempatan -= 1
        print(f"PIN salah! Sisa kesempatan: {kesempatan}")
        if kesempatan == 0:
            print("Kesempatan habis. Kartu terblokir.")
            exit()

# Menu utama
while True:
    print("\n=== Menu ATM ===")
    print("1. Lihat Saldo")
    print("2. Tarik Uang")
    print("3. Deposit")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        print(f"Saldo Anda: Rp{saldo:,}")

    elif pilihan == "2":
        tarik = int(input("Masukkan jumlah penarikan: Rp"))
        if tarik <= saldo:
            saldo -= tarik
            print(f"Berhasil tarik Rp{tarik:,}. Sisa saldo: Rp{saldo:,}")
        else:
            print("Saldo tidak cukup!")

    elif pilihan == "3":
        setor = int(input("Masukkan jumlah deposit: Rp"))
        saldo += setor
        print(f"Berhasil deposit Rp{setor:,}. Saldo sekarang: Rp{saldo:,}")

    elif pilihan == "4":
        print("Terima kasih telah menggunakan ATM ini.")
        break

    else:
        print("Menu tidak valid, silakan coba lagi.")
