# 3 CARA MEMAKAI INPUT DI PYTHON

# Cara 1
nama = input("Masukkan nama kamu: ")
print("Halo,", nama)

print("-" * 40)

# Cara 2
umur = int(input("Masukkan umur kamu: "))
print("Umur kamu tahun depan:", umur + 1)

print("-" * 40)

# Cara 3
x, y = map(int, input("Masukkan dua angka (pisahkan dengan spasi): ").split())
print("Jumlah kedua angka:", x + y)

print("-" * 40)

print("Terima kasih! Sekarang kamu tahu 3 cara memakai input() di Python.")
