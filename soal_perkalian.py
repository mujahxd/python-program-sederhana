import random

jumlah_soal = 5
skor = 0

print("=== Latihan Perkalian 2 Digit ===")
print(f"Akan ada {jumlah_soal} soal.\n")


for i in range(1, jumlah_soal + 1):
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    jawaban_benar = a * b

    jawaban_user = int(input(f"Soal {i}: {a} x {b} = "))

    if jawaban_user == jawaban_benar:
        print("Benar!\n")
        skor += 1
    else:
        print(f"Salah, Jawaban yang benar: {jawaban_benar}\n")


print(f"Selesai! Kamu menjawab benar {skor} dari {jumlah_soal} soal.")
