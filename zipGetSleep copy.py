# 3 Tips Python untuk Pemula 🚀
# ----------------------------------

# 🔹 TIP 1: Gunakan zip() untuk menggabungkan dua list
import time
nama = ["Ani", "Budi", "Cici"]
nilai = [90, 85, 88]

print("=== TIP 1: zip() ===")
for n, s in zip(nama, nilai):
    print(f"{n}: {s}")
print()  # baris kosong


# 🔹 TIP 2: Gunakan dict.get() agar aman saat ambil data
data = {"nama": "Dewi"}

print("=== TIP 2: dict.get() ===")
print("Nama:", data.get("nama", "Tidak diketahui"))
print("Umur:", data.get("umur", "Belum diisi"))
print()  # baris kosong


# 🔹 TIP 3: Gunakan time.sleep() untuk efek jeda

print("=== TIP 3: time.sleep() ===")
print("Hitung mundur:")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("Mulai!")
