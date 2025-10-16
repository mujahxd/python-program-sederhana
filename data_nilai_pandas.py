import pandas as pd

data = {
    "Nama": ["Alya", "Budi", "Citra", "Doni"],
    "Matematika": [85, 90, 78, 88],
    "Bahasa Inggris": [80, 75, 85, 92],
    "IPA": [89, 94, 76, 84]
}

df = pd.DataFrame(data)

print("=== Data Nilai Siswa ===")
print(df)

df["Rata-rata"] = df[["Matematika", "Bahasa Inggris", "IPA"]].mean(axis=1)
print("\n=== Setelah ditambah kolom rata-rata ===")
print(df)

top = df.loc[df["Rata-rata"].idxmax()]
print("\nSIswa dengan nilai rata-rata tertinggi:")
print(top["Nama"], "dengan rata-rata", round(top["Rata-rata"], 2))
