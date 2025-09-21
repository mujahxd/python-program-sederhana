import sys
import math


def permutasi(n, r):
    return math.factorial(n) // math.factorial(n - r)


def kombinasi(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


mode = sys.argv[1]
n = int(sys.argv[2])
r = int(sys.argv[3])

if mode == "permutasi":
    print(permutasi(n, r))
elif mode == "kombinasi":
    print(kombinasi(n, r))
