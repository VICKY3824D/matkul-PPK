 # LATIHAN 1

# daftar_harga = [];
# total_sell =  {};
# total = 0;
# rincian  = {};

# while True:
#     print("1. masukkan daftar harga");
#     print("2. tampilkan buah beserta harga");
#     print("3. jual");
#     print("4. rincian");
#     print("5. keluar sistem");
#     inp = int(input("Pilihan : "));
#     if  inp == 1:
#         buah = input("Buah : ");
#         harga = int(input("Harga : "));
#         daftar_harga.append([buah,harga]);
#     elif inp == 2:
#         print("daftar harga :", daftar_harga);
#     elif inp == 3:
#         print("Jual  buah : ");
#         buah = input("Buah : ");
#         for i in daftar_harga:
#             if buah == i[0]:
#                 jml = int(input("Jumlah : "));
#                 total_harga =  i[1] * jml;
#                 total_sell[buah] =  jml;
#                 total = total + total_harga;
#                 print(f"Buah {buah} terjual {jml} buah");
#                 break;
#             else:
#                 print("Buah tidak ada");

#     elif inp == 4:
#         print("Total pendapatan: Rp", total);
#         print("Rincian penjualan : ", total_sell);

#     elif inp == 5:
#         print("sistem selesai");
#         break;


# LATIHAN 2
# daftar_harga = [];
# daftar_diskon = [];
# total_sell =  {};
# total = 0;
# harga_stlh_disc  = {};

# while True:
#     print("1. masukkan daftar harga pakaian");
#     print("2. masukkan daftar diskon");
#     print("3. tampilkan pakaian beserta harga");
#     print("4. jual");
#     print("5. rincian");
#     print("6. keluar sistem");
#     inp = int(input("Pilihan : "));
#     if  inp == 1:
#         pakaian = input("Pakaian : ");
#         harga = int(input("Harga : "));
#         daftar_harga.append([pakaian,harga]);
#     elif  inp == 2:
#         barang = input("Pakaian  : ");
#         for i in daftar_harga:
#             if barang == i[0]:
#                 disc =  int(input("Diskon : "));
#                 hrg_after =i[1] * (100 - disc) / 100;
#                 harga_stlh_disc[barang] = hrg_after;
#                 print(f"harga pakaian {i[0]} setelah  diskon {disc}% adalah Rp {hrg_after}");
#                 break;
#             else:
#                 print("Pakaian tidak ada");        
#     elif inp == 3:
#         print("daftar harga :", daftar_harga);
#         print("Setelah disc: ",  harga_stlh_disc);

#     elif inp == 4:
#         print("Jual  pakaian : ");
#         clothes = input("pakaian : ");
#         for i in harga_stlh_disc:
#             if clothes == i:
#                 jml = int(input("Jumlah : "));
#                 total_harga =  harga_stlh_disc[i] * jml;
#                 total_sell[clothes] =  jml;
#                 total = total + total_harga;
#                 print(f"pakaian {clothes} terjual {jml} buah, total {total}");
#                 break;
#             else:
#                 print("Pakaian tidak ada");

#     elif inp == 5:
#         print("Total pendapatan: Rp", total);
#         print("Rincian penjualan : ", total_sell);

#     elif inp == 6:
#         print("sistem selesai");
#         break;


# LATIHAN 3

# anggota = {};
# daftar_buku = [];
# buku_buku = []

# while True:

#     print("----------------------------\njika keluar input : 0")
#     n = int(input("Memasukkan berapa orang : "));

#     if  n == 0:
#         break;
#     else:
#         for i in range(n):
#             print('-------------------')
#             nama = input("Nama : ");
#             nBuku = int(input("berapa buku : "));
            
#             if nama not in anggota:
#                 anggota[nama] = [];
            
#             for i in  range(nBuku):
#                 buku = input("Buku : ");
#                 anggota[nama].append(buku);

# print("data buku sebelum dihapus", anggota)

# while True:
#     print("\n----------------------------");
#     pilihan = input("Apakah ingin menghapus buku? (y/n) : ");

#     if pilihan.lower() == 'n':
#         break;
#     elif pilihan.lower() == 'y':
#         nama = input("Anggota yang ingin dihapus bukunya: ");
#         if nama in anggota:
#             buku = input("Masukkan judul buku yang ingin dihapus: ");
#             if buku in anggota[nama]:
#                 anggota[nama].remove(buku);
#                 print(f"Buku '{buku}' telah dihapus dari {nama}.");
#             else:
#                 print(f"Buku '{buku}' tidak ditemukan di daftar {nama}.");
#         else:
#             print(f"Nama '{nama}' tidak ditemukan.");
#     else:
#         print("Pilihan tidak valid(y/n).");
    
# print("data buku setelah dihapus: ", anggota);


# LATIHAN 4

reservasi = {};
n =  int(input("Masukkan jumlah meja: "));
for i in range(1, n+1):
    reservasi[i] = input(f"Nama yang memesan meja-{i}: ");
print("reservasi awal: ",reservasi);
jml_hps = int(input("banyak meja yang ingin dihapus:  "));
for i in range(jml_hps):
    hapus  = int(input("Meja yang ingin dihapus: "));
    if  hapus in reservasi:
        reservasi[hapus]  = "kosong";

    else:
        print("meja {hapus} tidak ada")
print(f"reservasi final:",reservasi)




