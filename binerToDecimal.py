def biner_ke_desimal(biner_str):
    desimal = 0
    panjang = len(biner_str)

    for i in range(panjang):
        bit = biner_str[i]
        if bit not in ('0', '1'):
            return None

        nilai = int(bit) * (2 ** (panjang - 1 - i))
        desimal += nilai

    return desimal


biner = input("Masukkan bilangan biner (misal: 1010): ")
hasil = biner_ke_desimal(biner)

if hasil is not None:
    print(f"Hasil desimal dari biner {biner} adalah: {hasil}")
else:
    print("Input tidak valid! Masukkan hanya angka 0 dan 1.")
