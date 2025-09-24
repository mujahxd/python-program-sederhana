from datetime import datetime

absensi = []

while True:
    nama = input("Masukkan nama (atau kosong untuk keluar): ").strip()
    if not nama:
        break

    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    absensi.append((nama, waktu))

    print("\nData Absensi:")
    print(f"{'No':<4} {'Nama':<20} {'Waktu Absen'}")
    for i, (n, w) in enumerate(absensi, start=1):
        print(f"{i:<4} {n:<20} {w}")
