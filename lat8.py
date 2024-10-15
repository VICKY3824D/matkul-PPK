# LATIHAN 1

# daftar_harga = [['apel',3000], ['pisang' , 2000], ['jeruk', 5000]];
# today_sell = {'apel' : 10, 'pisang': 5, 'jeruk': 3};
# total = 0;
# rincian  = {};

# sum_apel = daftar_harga[0][1]  * today_sell['apel'];
# sum_pisang = daftar_harga[1][1] * today_sell['pisang'];
# sum_jeruk = daftar_harga[2][1] * today_sell['jeruk'];

# rincian['apel'] =  sum_apel;
# rincian['pisang'] = sum_pisang;
# rincian['jeruk'] = sum_jeruk;

# total1 = sum_apel + sum_pisang + sum_jeruk;

# print("Total pendapatan: Rp", total);
# print("Rincian penjualan : ", rincian);


# LATIHAN 2
# daftar_pakaian = [['sepatu',  500000], ['tas', 300000], ['topi', 150000]];
# diskon = [10,20,5];

# harga_setelah_diskon = {};

# hrga_sepatu_disk = daftar_pakaian[0][1]  - (daftar_pakaian[0][1] * diskon[0] / 100);
# hrga_tas_disk = daftar_pakaian[1][1] - (daftar_pakaian[1][1] *  diskon[1] / 100);
# hrga_topi_disk = daftar_pakaian[2][1] - (daftar_pakaian[2][1]  * diskon[2] / 100);

# total2 =  hrga_sepatu_disk + hrga_tas_disk + hrga_topi_disk;

# harga_setelah_diskon['sepatu'] = hrga_sepatu_disk;
# harga_setelah_diskon['tas'] = hrga_tas_disk;
# harga_setelah_diskon['topi'] = hrga_topi_disk;

# print("Harga setelah diskon : ", harga_setelah_diskon);
# print("Total harga setelah diskon: Rp", total2)


# LATIHAN 3
# anggota = {'Ali':['Buku A', 'Buku B'], 'Budi': ['Buku C']};
# # tambah buku untuk ali 
# anggota['Ali'].append('Buku D');
# #  Hapus  buku C dari budi
# del  anggota['Budi'][0];
# print("Data pinjaman: ",anggota);

# LATIHAN 4

reservasi = {1 : 'Budi', 2 : 'Siti', 3 : 'Andi'};
# menambah reservasi
reservasi[4] = 'Joko';
# menghapus reservasi
del reservasi[2];
print("Status meja: ",reservasi);

