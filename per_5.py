#latihan 1
# n = int(input())
# if n % 4 == 0:
#     print("tahun kabisat")

# print("bukan tahun kabisat")


#latihan 2
# a = int(input())
# b = int(input())
# c = int(input())

# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else: 
#     print(c)

#latihan 2 (2)
# d = input().split()
# e = list(map(int, d))

# e1 = e[0]
# e2 = e[1]
# e3 = e[2]

# if e1 > e2 and e1 > e3:
#     print(e1)
# elif e2 > e1 and e2 > e3:
#     print(e2)
# else: 
#     print(e3)

    

# #quiz 1

# # Input bilangan pecahan dari pengguna
# bilangan = float(input("Masukkan bilangan pecahan: "))

# # Ambil bagian integer dan pecahan
# bagian_integer = int(bilangan)
# nilai_pecahan = bilangan - bagian_integer

# # Lakukan pembulatan berdasarkan nilai pecahan
# if nilai_pecahan >= 0.4:
#     hasil = bagian_integer + 1
# else:
#     hasil = bagian_integer

# # Tampilkan hasil pembulatan
# print("Hasil pembulatan:", hasil)


# #quiz 2
# # Program untuk menemukan nilai terbesar kedua di antara tiga input menggunakan percabangan

# # Menerima tiga input nilai dari pengguna
# nilai1 = float(input("Masukkan nilai pertama: "))
# nilai2 = float(input("Masukkan nilai kedua: "))
# nilai3 = float(input("Masukkan nilai ketiga: "))

# # Menemukan nilai terbesar kedua menggunakan percabangan
# if (nilai1 > nilai2 and nilai1 < nilai3) or (nilai1 > nilai3 and nilai1 < nilai2):
#     terbesar_kedua = nilai1
# elif (nilai2 > nilai1 and nilai2 < nilai3) or (nilai2 > nilai3 and nilai2 < nilai1):
#     terbesar_kedua = nilai2
# else:
#     terbesar_kedua = nilai3

# # Output nilai terbesar kedua
# print("Nilai terbesar kedua adalah:", terbesar_kedua)


#quiz 3
# Program untuk memeriksa apakah tanggal valid

# Menerima input tanggal, bulan, dan tahun dari pengguna
tanggal = int(input("Masukkan tanggal: "))
bulan = int(input("Masukkan bulan: "))
tahun = int(input("Masukkan tahun: "))

# Fungsi untuk memeriksa apakah tahun kabisat
def is_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

# Memeriksa validitas tanggal berdasarkan bulan
if bulan < 1 or bulan > 12:
    valid = False
else:
    # Daftar jumlah hari tiap bulan (Februari disesuaikan untuk tahun kabisat)
    if bulan == 2:  # Februari
        if is_kabisat(tahun):
            max_hari = 29
        else:
            max_hari = 28
    elif bulan in [4, 6, 9, 11]:  # April, Juni, September, November
        max_hari = 30
    else:  # Januari, Maret, Mei, Juli, Agustus, Oktober, Desember
        max_hari = 31

    # Memeriksa apakah tanggal valid
    if tanggal >= 1 and tanggal <= max_hari:
        valid = True
    else:
        valid = False

# Output apakah tanggal valid atau tidak
if valid:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah tanggal yang valid.")
else:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah tanggal yang tidak valid.")





#latihan perulangan 1

# halaman = int(input())
# hasil = 1

# i = 1
# while(i <= halaman):
#     hasil += 1
#     if i % 7 == 2:  hasil += 2
#     elif i % 7 == 0:   hasil += 3 
#     i += 1

# hari = hasil % 7

# def f(hari):
#     match hari:
#         case 1: return("Senin")
#         case 2: return("Selasa")
#         case 3: return("Rabu")
#         case 4: return("Kamis")
#         case 5: return("Jumat")
#         case 6: return("Sabtu")
#         case 0: return("Minggu")

# print(f(hari))

#latihan 2 perulangan
