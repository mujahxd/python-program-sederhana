def hitung_waktu_tempuh(jarak, kecepatan):
    if kecepatan <= 0:
        raise ValueError("Kecepatan harus lebih dari 0 km/jam.")
    waktu = jarak / kecepatan
    return waktu


def main():
    print("=== Program Menghitung Waktu Tempuh ===")

    try:
        jarak = float(input("Masukkan jarak (km): "))
        kecepatan = float(input("Masukkan kecepatan rata-rata (km/jam): "))

        waktu = hitung_waktu_tempuh(jarak, kecepatan)
        jam = int(waktu)
        menit = (waktu - jam) * 60

        print(f"\nPerkiraan waktu tempuh: {jam} jam {menit:.0f} menit")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
