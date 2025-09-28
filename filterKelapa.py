import sys


def filter_kelapa(nama_buah, diameter):
    if nama_buah.lower() != "kelapa":
        return "Invalid: hanya bisa filter kelapa"

    diameter = float(diameter)
    if diameter < 10:
        return "Kecil"
    elif 10 <= diameter <= 15:
        return "Sedang"
    else:
        return "Besar"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python filterKelapa.py <nama_buah> <diameter>")
        sys.exit(1)

    nama_buah = sys.argv[1]
    diameter = sys.argv[2]

    try:
        hasil = filter_kelapa(nama_buah, diameter)
        print("Ukuran:", hasil)
    except ValueError:
        print("Diameter harus berupa angka!")
