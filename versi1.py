print("Sistem Apotek \n\n1. Tambah Obat")
print("2. Lihat Struk Obat \n3. Hapus Obat")
print("4. Jual Obat \n5. Laporan Transaksi ")
print("6. Peringatan stok rendah")
obat = []
while True:
    
    menu  = int(input("pilih menu: "))
    if menu == 1:
   
        nama_obat = input("masukkan nama obat: ").lower()
        harga_obat = float(input("masukkan harga obat: "))
        stok_obat = int(input("masukkan stok obat: "))
        kadaluarsa = input("Tanggal kadaluarsa: ")
        daftar_obat = [nama_obat,harga_obat,stok_obat,kadaluarsa]
        obat.append(daftar_obat)
        print(f"obat {nama_obat}  berhasil ditambahkan dengan stok {stok_obat}")
    elif menu == 2:
        if len(obat) > 0:
            for i in obat: 
                print("========") 
                print("Nama Obat: ", daftar_obat[0]) 
                print("Harga Obat: ", daftar_obat[1]) 
                print("Stok Obat: ", daftar_obat[2]) 
                print("Tanggal Kadaluarsa: ", daftar_obat[3]) 
                print("========")  
        else:
            print("Belum ada obat yang ditambahkan.")
    elif menu == 3:
        hapus = input("Hapus obat mana : ").lower()
        for j in obat:
            if hapus in j:
                obat.remove(j)
                print(f"obat {hapus} telah berhasi dihapus")
    
    # #Menjual obat     
    # elif menu == 4:         
    #     jual = input("Jual obat: ").lower()    
    #     jumlah = int(input("jumlah: ")) 
    #     for j in obat:            
    #         if jual in j:                 
    #             stok_obat = stok_obat - jumlah                
    #             print(f"{jual} terjual sebanyak {jumlah} unit. sisa stok: {stok_obat}")  #bug: stok tidak berkurang     
                                   
    #     total = jumlah *  harga_obat         
    #     print(f"struk: {jual}, jumlah: {jumlah}, total : {total}") 
    