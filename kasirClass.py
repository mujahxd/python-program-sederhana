class Item:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga


class Kasir:
    def __init__(self):
        self.keranjang = []

    def tambah_item(self, item):
        self.keranjang.append(item)

    def lihat_item(self):
        if not self.keranjang:
            print("Keranjang masih kosong.")
        else:
            print("\n=== Daftar Barang yang Dibeli ===")
            for i, item in enumerate(self.keranjang, 1):
                print(f"{i}. {item.nama} - Rp{item.harga}")
            print("================================")
            print(f"Total: Rp{self.total()}")

    def total(self):
        return sum(item.harga for item in self.keranjang)


kasir = Kasir()

kasir.tambah_item(Item("Roti", 10000))
kasir.tambah_item(Item("Susu", 8000))
kasir.tambah_item(Item("Telur", 15000))

kasir.lihat_item()
