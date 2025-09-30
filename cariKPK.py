import math


def kpk(*numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result = abs(result * n) // math.gcd(result, n)
    return result


data = list(
    map(int, input("Masukkan beberapa bilangan (pisahkan dengan spasi): ").split()))

hasil = kpk(*data)
print(f"KPK dari {data} adalah {hasil}")
