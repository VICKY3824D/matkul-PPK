print("Sistem Apotek \n\n1. Tambah Obat")
print("2. Lihat Struk Obat \n3. Hapus Obat")
print("4. Jual Obat \n5. Laporan Transaksi ")
print("6. Peringatan stok rendah")
obat = []
while True:
    
    menu  = int(input("pilih menu: "))
    menu.lower()
    if menu == 1:
   
        nama_obat = input("masukkan nama obat: ")
        harga_obat = int(input("masukkan harga obat: "))
        stok_obat = int(input("masukkan stok obat: "))
        kadaluarsa = input("Tanggal kadaluarsa: ")
        obat.append(f"nama obat:{nama_obat}\nharga obat:{harga_obat}\nstok obat:{stok_obat}\nkadaluarasa:{kadaluarsa}")
        print(f"obat {nama_obat}  berhasil ditambahkan dengan stok {stok_obat}")
    elif menu == 2:
        if len(obat) > 0:
            for i in obat: 
                print("========") 
                print(i,end="\n") 
                print("========")  
        else:
            print("Belum ada obat yang ditambahkan.")
    elif menu == 3:
        hapus = input("Hapus obat mana : ")
        hapus.lower()
        for j in obat:
            if hapus in j:
                obat.remove(j)
                print(f"obat {hapus} telah berhasi dihapus")
    