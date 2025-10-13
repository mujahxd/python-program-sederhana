# Fungsi dengan jumlah argumen yang fleksibel
def total_semua(*angka):
    return sum(angka)


print(total_semua(2, 3))        # output: 5
print(total_semua(1, 2, 3, 4))  # output: 10


# Fungsi yang menerima pasangan key=value
def biodata(**data):
    for k, v in data.items():
        print(f"{k}: {v}")


biodata(nama="Mujahid", umur=18, kota="Jakarta")


# Fungsi yang mengembalikan beberapa hasil
def hitung(a, b):
    return a + b, a - b, a * b


tambah, kurang, kali = hitung(8, 3)
print(tambah, kurang, kali)  # output: 11 5 24
