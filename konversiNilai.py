def konversi_nilai(angka):
    if angka >= 85:
        return "A"
    elif angka >= 75:
        return "B"
    elif angka >= 65:
        return "C"
    elif angka >= 55:
        return "D"
    else:
        return "E"


print("=== KONVERSI NILAI ANGKA KE HURUF ===")

try:
    nilai = float(input("Masukkan nilai kamu: "))
    huruf = konversi_nilai(nilai)
    print(f"Nilai huruf kamu adalah: {huruf}")
except ValueError:
    print("Input tidak valid! Harus berupa angka.")
