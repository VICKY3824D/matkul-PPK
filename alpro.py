#latihan 1 dengan if else
# x = input("nilai matakuliah: ")
# if x == "A" or x == 'B':
#     print("Selamat, Anda Lulus!")
# elif x == "C":
#     print("lulus sebaiknya diulang")
# elif  x == "D":
#     print("lulus dan wajib diulang")
# else:
#     print("Tidak Lulus!")
    
# #latihan 1 dengan case
# y = input("nilai matakuliah: ")
# def f(y):
#     match y:
#         case "A" | "B":
#             return("Selamat, Anda Lulus!")
#         case "C":
#             return("lulus sebaiknya diulang ")
#         case "D":
#             return("lulus dan wajib diulang")
#         case "E":
#             return("Tidak Lulus!")

# print(f(y))
        
        
#latihan2
hari = input("Hari kuliah: ")

def f(hari):
    match hari:
        case "Senin":
            return("Kuliah Algoritma Struktur data jam 9")
        case "Selasa":
            return("Kuliah kalkulus 1 jam 7")
        case "Rabu":
            return("Kuliah Algoritma Struktur data jam 12")
        case "Kamis":
            jam = int(input('jam: '))
            if jam >= 7 and jam <= 9:
                return("kuliah pancasila di filsafat")
            elif jam >= 9 and jam <= 10:
                return("kosong")
            elif jam >= 10 and jam <= 12:
                return("Kuliah bahasa inggris I")
            elif jam >= 12 and jam <= 13:
                return("kosong")
            elif jam >= 13 and jam <= 15:
                return("Kuliah logika informatika")
            elif jam >= 15:
                return("kosong")
            
        case "Jumat":
            return("Kuliah Agama jam 9")
        case  "Sabtu":
            return("Tidak masuk hari kuliah weekday, Sabtu")
        case "Minggu":
            return("libur")

print(f(hari))