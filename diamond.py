import sys


def print_diamond(n):
    if n <= 0:
        sys.exit("Error: angka harus positif.")
    if n % 2 == 0:
        sys.exit("Error: angka harus ganjil.")

    for stars in range(1, n + 1, 2):
        print(" " * ((n - stars) // 2) + "*" * stars)

    for stars in range(n - 2, 0, -2):
        print(" " * ((n - stars) // 2) + "*" * stars)


if len(sys.argv) > 1:
    n = int(sys.argv[1])
    print_diamond(n)
