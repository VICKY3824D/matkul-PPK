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
    
    #menampilan obat
    elif menu == 2:
        if len(obat) > 0:
            for i, daftar_obat in enumerate(obat):
                print(f"Obat {i+1}:")
                print(f"  Nama: {daftar_obat[0]}")
                print(f"  Harga: {daftar_obat[1]}")
                print(f"  Stok: {daftar_obat[2]}")
                print(f"  Tanggal Kadaluarsa: {daftar_obat[3]}")
                print("========")  
        else:
            print("Belum ada obat yang ditambahkan.")
            
    #Menghapus obat
    elif menu == 3:
        hapus = input("Hapus obat mana : ").lower()
        for j in obat:
            if hapus in j:
                obat.remove(j)
                print(f"obat {hapus} telah berhasi dihapus")
    
    #Menjual obat     
    elif menu == 4:         
        jual = input("Jual obat: ").lower()    
        jumlah = int(input("jumlah: ")) 
        for j in obat:            
            if jual in j:                 
                j[2] = j[2] - jumlah                
                print(f"{jual} terjual sebanyak {jumlah} unit. sisa stok: {j[2]}")  #bug: stok tidak berkurang     
                                   
        total = jumlah *  harga_obat         
        print(f"struk: {jual}, jumlah: {jumlah}, total : {total}") 
    
    #laporan transaksi
    elif menu == 5:
        print("laporan keuangan")
    
    #pemberitahuan stok rendah
    elif menu == 6:
        batas_stok = 5  # Batas stok rendah
        stok_rendah = False
        
        print("Peringatan stok rendah:")
        for j in obat:
            if j[2] < batas_stok:
                print(f"Obat {j[0]} stok rendah. Sisa stok: {j[2]}")
                stok_rendah = True
        
        if not stok_rendah:
            print("Tidak ada obat dengan stok rendah.")
    
        # else:
        #     print("Menu tidak valid, silakan pilih menu yang benar.")
        
    #kadaluarsa
    elif menu == 7:
        checked = False
        # tgl = input("masukkan tanggal sekarang (yy-mm-dd): ")
        # tanggal_sekarang = tgl.split('-')
        
        tanggal, bulan, tahun = 20, 10, 2024
        
        for j in obat:
            tanggal_lalu = j[3].split('-')
            year = int(tanggal_lalu[0])
            month = int(tanggal_lalu[1])
            day = int(tanggal_lalu[2])
            if tahun > year:
                print(f"Obat {j[0]} telah kadaluarsa.")
            elif  tahun == year:
                if bulan > month:
                    print(f"Obat {j[0]} telah kadaluarsa.")
                elif tanggal ==  day:
                    print(f"Obat {j[0]} telah kadaluarsa.")
            else:
                print("tidak ada yang kadaluarsa")
                
                    