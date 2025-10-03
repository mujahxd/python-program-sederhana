import sys
from statistics import mean, median


def baca_data(namafile):
    with open(namafile, 'r') as f:
        isi = f.read()
    data = [float(x) for x in isi.split()]
    return data


def main():
    if len(sys.argv) != 2:
        print("Cara pakai: python mean_median.py <nama_file>")
        sys.exit(1)

    namafile = sys.argv[1]
    data = baca_data(namafile)

    hasil_mean = round(mean(data), 2)
    hasil_median = round(median(data), 2)

    print(f"Mean: {hasil_mean}")
    print(f"Median: {hasil_median}")


if __name__ == "__main__":
    main()
