buah = ["apel", "mangga", "jeruk", "semangka"]
panjang = []
for b in buah:
    if len(b) > 5:
        panjang.append(b)
print(f"tanp comprehension: {panjang}")


panjang = [b for b in buah if len(b) > 5]
print(f"dengan comprehension: {panjang}")
