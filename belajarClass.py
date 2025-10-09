# membuat class Siswa dengan atribut nama dan umur

class Siswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    # menambahkan method ke dalam class
    def perkenalan(self):
        return f"Halo, saya {self.nama}, umur {self.umur} tahun."


# membuat objek dari class
s1 = Siswa("Andi", 15)

print(s1.perkenalan())
