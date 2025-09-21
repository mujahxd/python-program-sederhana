print("Kalkulator input satu-satu (angka dan operator)")
hasil = float(input("Masukkan angka pertama: "))

while True:
    operator = input("Masukkan operator (+, -, *, /) atau 's' untuk selesai: ")

    if operator == 's':
        break

    if operator not in ['+', '-', '*', '/']:
        print("Operator tidak valid, coba lagi.")
        continue

    angka_selanjutnya = float(input("Masukkan angka berikutnya: "))

    if operator == '+':
        hasil += angka_selanjutnya
    elif operator == '-':
        hasil -= angka_selanjutnya
    elif operator == '*':
        hasil *= angka_selanjutnya
    elif operator == '/':
        if angka_selanjutnya == 0:
            print("Error: tidak bisa membagi dengan nol!")
            continue
        hasil /= angka_selanjutnya

    print(f"Hasil sementara: {hasil:,.3f}")

print(f"Hasil akhir: {hasil:,.3f}")
