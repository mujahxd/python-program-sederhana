jumlah = int(input("Masukkan banyak nilai yang diinput: "))

if jumlah == 0:
    print("Tidak ada nilai yang diinput, rata-rata tidak bisa dihitung.")
else:
    total = 0

    for i in range(jumlah):
        nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
        total += nilai

    rata_rata = total / jumlah

    print(f"Rata-rata nilai: {rata_rata:.2f}")
