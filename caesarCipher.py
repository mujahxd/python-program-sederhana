import sys


def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                base = ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


if len(sys.argv) < 3:
    print("Usage: python caesarCipher.py <shift> <text>")
    print("Contoh: python caesarCipher.py 3 Halo Dunia")
    sys.exit(1)

shift = int(sys.argv[1])
text = " ".join(sys.argv[2:])

hasil = caesar_cipher(text, shift)

print(f"Teks asli: {text}")
print(f"Result: {hasil}")
