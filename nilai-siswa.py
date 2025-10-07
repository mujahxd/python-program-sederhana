nilai = {
    "Ali": 85,
    "Budi": 90,
    "Citra": 78
}

print("=== Data Awal ===")
print(nilai)
print()

# 1. .get() - Ambil nilai aman tanpa error
print("1. Mengambil nilai siswa dengan .get()")
print("Nilai Budi:", nilai.get("Budi"))
print("Nilai Dina:", nilai.get("Dina", "Data tidak ditemukan"))
print()

# 2. .update() - Perbarui nilai siswa
print("2. Memperbarui nilai siswa dengan .update()")
print("Citra remedial, nilainya berubah jadi 88")
nilai.update({"Citra": 88})
print("Data terbaru:", nilai)
print()

# 3. pop() - Hapus data siswa tertentu
print("3. Menghapus data siswa dengan .pop()")
terhapus = nilai.pop("Ali")
print(f"Data '{terhapus}' dihapus. Sisa data:", nilai)
print()

print("== Program selesai ===")
