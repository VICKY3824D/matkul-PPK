# Input jumlah kegiatan
N = int(input("Masukkan batas  peserta untuk gedung A: "))
jumlah_kegiatan = int(input("Masukkan jumlah kegiatan dalam 1 hari: "))

kapasitas_A = 5
kapasitas_B = 3

sum_kegiatan_A = 0
sum_kegiatan_B = 0

for i in range(jumlah_kegiatan):
    peserta = int(input(f"Masukkan peserta kegiatan ke-{i + 1}: "))

    if peserta < N and sum_kegiatan_A < kapasitas_A:
        sum_kegiatan_A += 1
        print(f"banyak kegiatan di A : {sum_kegiatan_A}")

    elif sum_kegiatan_B < kapasitas_B:
        sum_kegiatan_B += 1
        print(f"banyak kegiatan di B : {sum_kegiatan_B}")

    else:
        print(f"Kegiatan ke-{i + 1} tidak dapat dilaksanakan, Gedung B sudah penuh.")
        break

print(f"Total kegiatan di Gedung A: {sum_kegiatan_A}")
print(f"Total kegiatan di Gedung B: {sum_kegiatan_B}")
