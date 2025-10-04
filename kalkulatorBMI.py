def hitung_bmi(berat, tinggi):
    tinggi_m = tinggi / 100
    bmi = berat / (tinggi_m ** 2)
    return bmi


def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Gemuk"
    else:
        return "Obesitas"


berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (cm): "))

bmi = hitung_bmi(berat, tinggi)
kategori = kategori_bmi(bmi)

print(f"\nBMI kami: {bmi:.2f}")
print(f"Kategori: {kategori}")
