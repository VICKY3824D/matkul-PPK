#vidky A2
#davena
#Rizendy
#Muhammad Diya

print("=============")
print("Sistem Apotek")
print("=============")
obat = [] # inisialisasi list obat 
# obat_terjual =  [] #mendata obat yang terjual
obat_dijual = []
omset = 0 #mendata omzet

# Function to check if the medicine is expired
def is_kadaluarsa(name, yy, mm, dd):
    for j in obat:
        if j[0].lower() == name.lower():  # match the medicine name (ignoring case)
            # Memisahkan tanggal kadaluarsa obat
            tanggal_lalu = j[3].split('-')
            tahun_kadaluarsa = int(tanggal_lalu[0])
            bulan_kadaluarsa = int(tanggal_lalu[1])
            hari_kadaluarsa = int(tanggal_lalu[2])

            # Logika pengecekan kadaluarsa
            if tahun_kadaluarsa < yy:
                return True  # Obat kadaluarsa
            elif tahun_kadaluarsa == yy:
                if bulan_kadaluarsa < mm:
                    return True  # Obat kadaluarsa
                elif bulan_kadaluarsa == mm:
                    if hari_kadaluarsa <= dd:
                        return True  # Obat kadaluarsa
                    else:
                        return False  # Obat belum kadaluarsa
                else:
                    return False  # Obat belum kadaluarsa
            else:
                return False  # Obat belum kadaluarsa

    return None  # Return None if the medicine name is not found

# Function to handle selling medicine
def jual_obat():
    jual = input("Jual obat: ").lower()
    
    # Masukkan tanggal saat ini untuk pengecekan kadaluarsa
    tgl_sekarang = input("Masukkan tanggal sekarang (yyyy-mm-dd): ")
    tahun_sekarang, bulan_sekarang, hari_sekarang = map(int, tgl_sekarang.split('-'))

    # Cek apakah obat sudah kadaluarsa
    if is_kadaluarsa(jual, tahun_sekarang, bulan_sekarang, hari_sekarang):
        print(f"Obat {jual} sudah kadaluarsa dan tidak dapat dijual.")
    else:
        jumlah = int(input("Jumlah: ")) 
        member = input("member atau bukan (y/n?): ").lower()

        for j in obat:
            if jual == j[0]:  # memerikas apakah nama obat sesuai yang diinputkan
                if j[2] >= jumlah:  # memastikan stok cukup
                    j[2] -= jumlah  # mengurangi stok
                    print(f"{jual} terjual sebanyak {jumlah} unit. Sisa stok: {j[2]}")
                    
                    jualan = [jual, jumlah]  # mengelist data penjualan
                    obat_dijual.append(jualan)  # Masukkan penjualan ke list obat_dijual
                    
                    total = jumlah * j[1]  # total belanja
                    print(f"struk: {jual}, jumlah: {jumlah}, total : {total}")

                    if member == 'y':
                        discount = total * 0.1  # Diskon member 10%
                        total -= discount  # Mengurangi total dengan diskon
                        print(f"Dengan diskon sebesar member {discount}")

                    if total > 100000:  # Diskon tambahan jika total belanja melebihi 100.000
                        diskon = total * 0.1  # Diskon tambahan 10%
                        total -= diskon
                        print(f"Dengan diskon 10% sebesar {diskon}")
                    
                    global omset  # Menggunakan omset dari luar fungsi
                    omset += total  # Menambah omset setiap penjualan
                    print(f"struk: {jual}, jumlah: {jumlah}, total : {total}")
                    break  # Keluar dari loop setelah penjualan berhasil
                else:
                    print(f"Stok {jual} tidak cukup")
                    break
        else:
            print(f"Obat {jual} tidak ada.")


while True:
    
        print("-------------") 
        print("1. Tambah Obat")
        print("2. Lihat Struk Obat \n3. Hapus Obat")
        print("4. Jual Obat \n5. Laporan Transaksi ")
        print("6. Peringatan stok rendah\n7. Cek kadaluarsa")
        print("10. Selesai")
        menu  = int(input("pilih menu(wajib angka): "))
        # memasukkan data obat
        if menu == 1:
        
            nama_obat = input("masukkan nama obat: ").lower()
            harga_obat = float(input("harga obat: "))
            stok_obat = int(input("stok obat: "))
            kadaluarsa = input("kadaluarsa (yyyy-mm-dd): ")
            daftar_obat = [nama_obat,harga_obat,stok_obat,kadaluarsa]
            obat.append(daftar_obat)
            print(f"obat {nama_obat}  berhasil ditambahkan dengan stok {stok_obat}")

        #menampilan obat
        elif menu == 2:
            if len(obat) > 0:
                for i, daftar_obat in enumerate(obat):
                    print("----------") 
                    print(f"Obat {i+1}:")
                    print(f"  Nama: {daftar_obat[0]}")
                    print(f"  Harga: {daftar_obat[1]}")
                    print(f"  Stok: {daftar_obat[2]}")
                    print(f"  Tanggal Kadaluarsa: {daftar_obat[3]}")
                    print("----------")  
            else:
                print("Belum ada obat yang ditambahkan.")

        #Menghapus obat
        elif menu == 3:
            hapus = input("Hapus obat mana : ").lower()
            for j in obat:
                if hapus in j:
                    obat.remove(j) # menghapus list obat pad hapus
                    print(f"obat {hapus} telah berhasi dihapus")
                else:
                    print(f"obat {hapus} tidak ada")

    
        #Menjual obat      
        elif menu == 4:
            jual_obat();         

           
        #laporan transaksi
        elif menu == 5:
            if len(obat_dijual) == 0:
                print("Belum ada obat yang terjual.")            
            else:
                print(f"obat yang terjual: ", end=" ")
                for i in obat_dijual:
                    print(f"{i[0]}({i[1]})",end=", ")
                print(f"\npenghasilan total: ", omset) 
                
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
            # checked = False
            tgl = input("Masukkan tanggal sekarang (yyyy-mm-dd): ")
            tanggal_sekarang = list(tgl.split('-'))

            # Memisahkan input tanggal sekarang
            tahun_sekarang = int(tanggal_sekarang[0])
            bulan_sekarang = int(tanggal_sekarang[1])
            hari_sekarang = int(tanggal_sekarang[2])
            
            for i in obat:
                if is_kadaluarsa(i[0],tahun_sekarang,  bulan_sekarang, hari_sekarang) ==  True:
                    print(f"obat {i[0]} kadaluarsa")
                else:
                    print(f"obat {i[0]} tidak kadaluarsa")

        elif menu == 10:
            print("PROGRAM BERHENTI")
            break
        
  

    
    
                
                    