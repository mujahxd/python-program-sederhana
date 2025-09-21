import random

jarak_kota = {
    "B": 5,
    "C": 10,
    "D": 15,
    "E": 8,
    "F": 12
}

TARIF_PER_KM = 3000
DISKON_PILIHAN = [0, 10, 20, 50]

print("=== OJOL SEDERHANA ===")
print("Tujuan tersedia:", ", ".join(jarak_kota.keys()), "\n")

while True:
    tujuan = input("Masukkan tujuan (B-F): ").upper()

    jarak = jarak_kota[tujuan]
    harga_awal = jarak * TARIF_PER_KM
    diskon = random.choice(DISKON_PILIHAN)
    potongan = harga_awal * diskon / 100
    harga_akhir = harga_awal - potongan

    print(f"\nHarga awal: Rp{harga_awal:,.0f}")
    print(f"Diskon yang didapat: {diskon}%")
    print(f"Total bayar: Rp{harga_akhir:,.0f}")

    lanjut = input("\nMau lanjut pesan lagi? (y/n): ").lower()
    if lanjut != "y":
        print("\nTerima kasih sudah menggunakan OJOL sederhana!")
        break

    print("")
