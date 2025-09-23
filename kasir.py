keranjang = []
total = 0

n = int(input("Masukkan jumlah barang: "))

for i in range(n):
    nama = input(f"Nama barang {i+1}: ")
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
    subtotal = harga * jumlah
    keranjang.append((nama, jumlah, subtotal))
    total += subtotal

print("\n=== Struk Belanja ===")
for item in keranjang:
    print(f"{item[0]} x{item[1]} = Rp{item[2]:,}")
print(f"Total: Rp{total:,}")

bayar = int(input("Uang bayar: "))
print(f"Kembali: Rp{bayar - total:,}")
