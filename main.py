import random

angka_rahasia = random.randint(1, 100)
percobaan = 1

while True:
    tebakan = int(input(f"Tebakan ke-{percobaan} - Masukkan angka: "))

    if tebakan < angka_rahasia:
        print("Terlalu rendah\n")
    elif tebakan > angka_rahasia:
        print("Terlalu tinggi\n")
    else:
        print(
            f"\nBenar! Anda menebak angka {angka_rahasia} dalam {percobaan} percobaan.")
        break

    percobaan += 1
