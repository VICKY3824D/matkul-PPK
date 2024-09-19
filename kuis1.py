print("mulai")
jam_mulai = int(input())
menit_mulai = int(input())
detik_mulai = int(input())
print("selesai")
jam_selesai = int(input())
menit_selesai = int(input())
detik_selesai = int(input())

waktu_jam = jam_selesai - jam_mulai
waktu_menit = menit_selesai - menit_mulai
waktu_detik = detik_selesai - detik_mulai

d1 = waktu_jam * 3600
d2 = waktu_menit * 60
d3 = waktu_detik 

total_detik = d1 + d2 + d3

tampilan_jam = int(total_detik / 3600)
if tampilan_jam < 1:
    tampilan_menit = int(total_detik / 60)
    if tampilan_menit < 1:
        tampilan_detik = total_detik
    else:
        tampilan_detik = total_detik - tampilan_menit*60
elif tampilan_jam >= 1:
    tampilan_menit = int((total_detik - tampilan_jam*3600)/60)
    if tampilan_menit < 1:
        tampilan_detik = total_detik
    else:
        tampilan_detik = total_detik - tampilan_jam*3600 - tampilan_menit*60
    
    
print(tampilan_jam, tampilan_menit, tampilan_detik)