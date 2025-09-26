sayuran = {"Bayam": 5000, "Tomat": 12000, "Wortel": 8000, "Cabai": 30000}
keranjang = []

while True:
    print("\n=== Daftar Sayur ===")
    for i, (nama, harga) in enumerate(sayuran.items(), 1):
        print(f"{i}. {nama} - Rp{harga}/kg")

    pilihan = input("Pilih nomor sayur (q untuk checkout): ")
    if pilihan == "q":
        break

    nama, harga = list(sayuran.items())[int(pilihan) - 1]
    qty = float(input(f"Masukkan jumlah {nama} (kg): "))
    keranjang.append((nama, qty, harga * qty))

print("\n=== Keranjang ===")
total = 0
for nama, qty, subtotal in keranjang:
    print(f"- {nama} {qty}kg = Rp{subtotal}")
    total += subtotal
print(f"Total: Rp{total}")
