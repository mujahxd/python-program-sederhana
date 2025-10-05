import tkinter as tk
from logic import GameTebakAngka


class TebakAngkaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Tebak Angka")

        # Ukuran jendela
        lebar = 300
        tinggi = 200

        # Hitung posisi tengah layar
        screen_lebar = self.root.winfo_screenwidth()
        screen_tinggi = self.root.winfo_screenheight()
        posisi_x = (screen_lebar // 2) - (lebar // 2)
        posisi_y = (screen_tinggi // 2) - (tinggi // 2)

        # Set ukuran + posisi tengah
        self.root.geometry(f"{lebar}x{tinggi}+{posisi_x}+{posisi_y}")

        # Buat instance game
        self.game = GameTebakAngka()

        # Komponen GUI
        self.label = tk.Label(root, text="Tebak angka (1-100):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.btn_tebak = tk.Button(root, text="Tebak", command=self.tebak)
        self.btn_tebak.pack(pady=10)

        # Label hasil
        self.label_hasil = tk.Label(
            root, text="", fg="blue", font=("Arial", 10, "bold"))
        self.label_hasil.pack(pady=5)

        # Simpan pesan terakhir & id timer
        self.last_message = ""
        self.timer_id = None

    def tampilkan_hasil(self, teks, warna):
        """Render ulang label hasil dan auto-hilang setelah 2 detik"""
        # Hapus timer sebelumnya biar tidak bentrok
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        # Jika teks sama, tambahkan spasi agar Tkinter mau render ulang
        if teks == self.last_message:
            teks += " "

        self.label_hasil.config(text=teks, fg=warna)
        self.last_message = teks.strip()

        # Atur timer untuk hapus teks setelah 2 detik (2000 ms)
        self.timer_id = self.root.after(
            2000, lambda: self.label_hasil.config(text=""))

    def tebak(self):
        try:
            tebakan = int(self.entry.get())
            hasil = self.game.cek_tebakan(tebakan)

            if hasil == "Benar!":
                self.tampilkan_hasil("🎉 Selamat! Tebakanmu benar!", "green")
                self.game.reset()
                self.entry.delete(0, tk.END)
            elif hasil == "Terlalu kecil!":
                self.tampilkan_hasil("Terlalu kecil!", "red")
            elif hasil == "Terlalu besar!":
                self.tampilkan_hasil("Terlalu besar!", "red")
        except ValueError:
            self.tampilkan_hasil("Masukkan angka yang valid!", "orange")
