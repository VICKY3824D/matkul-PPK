print("Sistem Apotek \n\n1. Tambah Obat")
print("2. Lihat Struk Obat \n3. Hapus Obat")
print("4. Jual Obat \n5. Laporan Transaksi ")
print("6. Peringatan stok rendah")
obat = []
while True:
    
    menu  = int(input("pilih menu: "))
    if menu == 1:
        nama_obat = input("masukkan nama obat: ")
        harga_obat = int(input("masukkan harga obat: "))
        stok_obat = int(input("masukkan stok obat: "))
        kadaluarsa = input("Tanggal kadaluarsa: ")
        obat.append(f"{nama_obat.lower()}, {harga_obat}, {stok_obat}, {kadaluarsa}")
        print(f"obat {nama_obat}  berhasil ditambahkan dengan stok {stok_obat}")
    elif menu == 2:
        if len(obat) > 0:
            for i in obat: 
                nama,harga,stok,kadalwarsa= i.split(', ')
                print("========") 
                print('nama: ', nama) 
                print('harga: ', harga) 
                print('stok: ', stok)
                print('kadaluarsa:  ', kadalwarsa) 
                print("========")  
        else:
            print("Belum ada obat yang ditambahkan.")
    elif menu == 3:
        hapus = input("Hapus obat mana : ")
        hapus=hapus.lower()
        for j in obat:
            if hapus in j:
                obat.remove(j)
                print(f"obat {hapus} telah berhasi dihapus")
    
    #Menjual obat     
    elif menu == 4:         
        jual = input("Jual obat: ").lower()       
        jumlah = int(input("jumlah: "))
        datake =0         
        for i in obat: 
            nama,harga,stok,kadalwarsa= i.split(', ')
            datake+=1
            if jual==nama:
                stok=int(stok)
                stok=stok-jumlah
                obat[datake]=f"{nama}, {harga}, {stok}, {kadalwarsa} "
        total=jumlah*int(harga)
        print(f"{jual} terjual sebanyak {jumlah} unit. sisa stok: {stok}")
        print(f"struk: {jual}, jumlah: {jumlah}, total : {total}")
        