# sistem.py

from siswa import Siswa


class SistemInformasiSiswa:
    def __init__(self):
        self.data_siswa = []

    # ======== Input Terpisah ========
    def input_nis(self):
        while True:
            try:
                nis = int(input("Masukkan NIS (angka & unik): "))
                if any(s.nis == nis for s in self.data_siswa):
                    print("❌ NIS sudah terdaftar, masukkan NIS lain.")
                    continue
                return nis
            except ValueError:
                print("❌ NIS harus berupa angka!")

    def input_umur(self):
        while True:
            try:
                umur = int(input("Masukkan Umur: "))
                return umur
            except ValueError:
                print("❌ Umur harus berupa angka!")

    def input_jk(self):
        while True:
            jk = input("Masukkan Jenis Kelamin (L/P): ").upper()
            if jk in ["L", "P"]:
                return jk
            print("❌ Jenis kelamin harus 'L' atau 'P'.")

    # ======== Fitur Utama ========
    def tambah_siswa(self):
        print("\n=== Tambah Data Siswa ===")

        nis = self.input_nis()
        nama = input("Masukkan Nama: ").strip()
        kelas = input("Masukkan Kelas: ").strip()
        umur = self.input_umur()
        jk = self.input_jk()

        siswa = Siswa(nis, nama, kelas, umur, jk)
        self.data_siswa.append(siswa)
        print("✅ Data siswa berhasil ditambahkan!")

    def lihat_siswa(self):
        print("\n=== Daftar Data Siswa ===")
        if not self.data_siswa:
            print("Belum ada data siswa.")
        else:
            print(f"{'NIS':<10} {'Nama':<20} {'Kelas':<10} {'Umur':<5} {'JK':<3}")
            print("-" * 50)
            for s in self.data_siswa:
                print(
                    f"{s.nis:<10} {s.nama:<20} {s.kelas:<10} {s.umur:<5} {s.jk:<3}")

    # ======== Menu ========
    def menu_utama(self):
        while True:
            print("\n=== MENU UTAMA ===")
            print("1. Tambah Siswa")
            print("2. Lihat Data Siswa")
            print("3. Keluar")

            pilihan = input("Pilih menu (1-3): ")

            if pilihan == "1":
                self.tambah_siswa()
            elif pilihan == "2":
                self.lihat_siswa()
            elif pilihan == "3":
                print("Terima kasih! Program selesai.")
                break
            else:
                print("❌ Pilihan tidak valid, coba lagi.")
