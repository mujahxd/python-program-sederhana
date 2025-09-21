import math


def luas_segitiga():
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    return 0.5 * alas * tinggi


def luas_lingkaran():
    r = float(input("Masukkan jari-jari lingkaran: "))
    return math.pi * r * r


def luas_persegi_panjang():
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    return panjang * lebar


while True:
    print("\n=== Program Hitung Luas Bangun Datar ===")
    print("1. Segitiga")
    print("2. Lingkaran")
    print("3. Persegi Panjang")
    print("Ketik 'exit' untuk keluar")

    pilihan = input("Pilih bangun datar: ").lower()

    if pilihan == 'exit':
        print("Program selesai.")
        break
    elif pilihan == '1':
        print("Luas segitiga =", luas_segitiga())
    elif pilihan == '2':
        print("Luas lingkaran =", luas_lingkaran())
    elif pilihan == '3':
        print("Luas persegi panjang =", luas_persegi_panjang())
    else:
        print("Pilihan tidak valid, coba lagi.")
