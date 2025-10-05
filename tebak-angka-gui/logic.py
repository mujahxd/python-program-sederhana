import random


class GameTebakAngka:
    def __init__(self, batas_bawah=1, batas_atas=100):
        self.batas_bawah = batas_bawah
        self.batas_atas = batas_atas
        self.angka_rahasia = random.randint(self.batas_bawah, self.batas_atas)

    def reset(self):
        self.angka_rahasia = random.randint(self.batas_bawah, self.batas_atas)

    def cek_tebakan(self, tebakan: int) -> str:
        if tebakan < self.angka_rahasia:
            return "Terlalu kecil!"
        elif tebakan > self.angka_rahasia:
            return "Terlalu besar!"
        else:
            return "Benar!"
