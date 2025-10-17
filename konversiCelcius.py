import sys


def c2f(c):
    return (c * 9/5) + 32


def c2k(c):
    return c + 273.15


def c2r(c):
    return c * 4/5


def main():
    konversi = sys.argv[1].lower()

    nilai = float(sys.argv[2])

    if konversi == "c2f":
        hasil = c2f(nilai)
        print(f"{nilai} C = {hasil:.2f} F")
    elif konversi == "c2k":
        hasil = c2k(nilai)
        print(f"{nilai} C = {hasil:.2f} K")
    elif konversi == "c2r":
        hasil = c2r(nilai)
        print(f"{nilai} C = {hasil:.2f} R")


if __name__ == "__main__":
    main()
