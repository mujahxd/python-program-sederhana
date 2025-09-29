import sys
import string
import secrets

panjang = int(sys.argv[1])

if panjang < 8:
    print("Panjang minimal adalah 8 karakter!")
    sys.exit(1)

chars = string.ascii_letters + string.digits + string.punctuation

password = ""

for _ in range(panjang):
    karakter_acak = secrets.choice(chars)
    password = password + karakter_acak

print(password)
