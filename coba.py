print("Sistem Apotek \n\n1. Tambah Obat") 
print("2. Lihat Struk Obat \n3. Hapus Obat") 
print("4. Jual Obat \n5. Laporan Transaksi ")
print("6. Peringatan stok rendah")

obat = []  # Daftar obat sebagai list dari dictionary

while True:
    menu = int(input("Pilih menu: "))

    # Menambah data obat
    if menu == 1:
        nama_obat = input("Masukkan nama obat: ").lower()
        harga_obat = int(input("Masukkan harga obat: "))
        stok_obat = int(input("Masukkan stok obat: "))
        kadaluarsa = input("Tanggal kadaluarsa: ")
        obat.append({
            "nama_obat": nama_obat,
            "harga_obat": harga_obat,
            "stok_obat": stok_obat,
            "kadaluarsa": kadaluarsa
        })
        print(f"Obat {nama_obat} berhasil ditambahkan dengan stok {stok_obat}")

    # Menampilkan data obat
    elif menu == 2:
        if len(obat) > 0:
            for i in obat:
                print("========")
                print(f"Nama Obat: {i['nama_obat']}")
                print(f"Harga Obat: {i['harga_obat']}")
                print(f"Stok Obat: {i['stok_obat']}")
                print(f"Kadaluarsa: {i['kadaluarsa']}")
                print("========")
        else:
            print("Belum ada obat yang ditambahkan.")

    # Menghapus data obat
    elif menu == 3:
        hapus = input("Hapus obat mana: ").lower()
        for j in obat:
            if hapus == j['nama_obat']:
                obat.remove(j)
                print(f"Obat {hapus} telah berhasil dihapus")
                break
        else:
            print(f"Obat {hapus} tidak ditemukan.")

    # Menjual obat
    elif menu == 4:
        jual = input("Jual obat: ").lower()
        jumlah = int(input("Jumlah: "))
        for j in obat:
            if jual == j['nama_obat']:
                if j['stok_obat'] >= jumlah:
                    j['stok_obat'] -= jumlah
                    total = jumlah * j['harga_obat']
                    print(f"{jual} terjual sebanyak {jumlah} unit. Sisa stok: {j['stok_obat']}")
                    print(f"Struk: {jual}, jumlah: {jumlah}, total: {total}")
                else:
                    print(f"Stok {jual} tidak mencukupi.")
                break
        else:
            print(f"Obat {jual} tidak ditemukan.")
