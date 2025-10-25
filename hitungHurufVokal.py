import sys

if len(sys.argv) < 2:
    print("Usage: python hitungHurufVokal.py [kalimat]")
    sys.exit(1)

kalimat = sys.argv[1]
vokal = "aiueoAIUEO"
jumlah = 0

for huruf in kalimat:
    if huruf in vokal:
        jumlah += 1

print(f"Jumlah huruf vokal: {jumlah}")
