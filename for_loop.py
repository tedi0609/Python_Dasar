# Belajar For Loop

from traceback import print_tb


pelanggan = ["tedi", "budi", "joko", "andi"]
pelanggan.append("kurniawan")
pelanggan.append("siska")

# Mengakses semua nama pelanggan ?
for nama in pelanggan:
    print("=========================")
    print(f"Nama Pelanggan : {nama}")
    print("=========================")
