# #konversi string ke integer/sebaliknya
# x = '121'
# x_new = int(x)
# y = 123
# y_n = str(y)
# # print(type(y_n))

# #konversi integer ke float /sebaliknya
# x = 123
# x1 = float(x)
# y1 = 12.3
# y2 = int(y1)
# # print(y2)

# #konversi boolean ke integer
# b = True
# b1 = int(b)

# s = 0
# s2 = bool(s)
# print(s2)


# #fungsi split
# tembak = "mau gak jadi pacar aku"
# tembak2 = tembak.split()
# print(tembak2)

#boolean
# benar = True
# salah = False


# #kuis 1
# x = input("masukkan x: ")
# x_new = str(x)
# digit1 = x_new[0]
# digit2 = x_new[1]
# digit3 = x_new[2]
# digit4 = x_new[3]

# digit1 = int(digit1)
# digit2 = int(digit2)
# digit3 = int(digit3)
# digit4 = int(digit4)

# hasil = digit1 + digit2 + digit3 + digit4 
# print(hasil)


# x = input("masukkan x: ")
# x_new = str.split(x)
# digit1 = x_new[0]
# digit2 = x_new[1]
# digit3 = x_new[2]
# digit4 = x_new[3]

# digit1 = int(digit1)
# digit2 = int(digit2)
# digit3 = int(digit3)
# digit4 = int(digit4)

# hasil = digit1 + digit2 + digit3 + digit4 
# print(hasil)


# x = input()
# x_new = x.split()
# print(x_new)
# hasil = int(x_new[0]) + int(x_new[1]) + int(x_new[2]) + int(x_new[3]) + int(x_new[4])
# print(hasil)


# x = input()
# x_new = list(map(int, x))
# print(x_new)
# hasil = int(x_new[0]) + int(x_new[1]) + int(x_new[2]) + int(x_new[3]) + int(x_new[4])
# print(hasil)


# #latihan 2
# # x = input()
# # x_new = x.split()
# # hasil = int(x_new[0]) + int(x_new[1]) + int(x_new[2]) + int(x_new[3]) + int(x_new[4])
# # print(hasil)

# #latihan 3


# #input integer
# x = int(input())

# #input string
# a = str(input())

# #input boolean
# b = bool(input())
# print(b)

# #output
# call = "sayang"
# gf = 'kamu'
# print(call, " ", gf)

#praktik
# PI = 3.14
# data = input("Masukkan jari-jari dan tinggi: ").split()
# data_float = list(map(float, data))
# jariJari = data_float[0]
# tinggi = data_float[1]
# luas = 2 * PI * jariJari * (jariJari + tinggi)
# print("luas permukaan : ",luas)

#latihan2
# x = input()
# x_new = x.split()
# y = input()
# y_new = y.split()

# itg1 = int(x_new[0])
# itg2 = int(x_new[1])
# itg3 = int(y_new[0])
# itg4 = int(y_new[1])
    
# hasil = (itg1 + itg2 + itg3 + itg4)
# print("hasil: ", hasil)

# dim = [[1,2],[5,3]]
# print(dim[1][0])

#matriks
x = input().split()
x1 = input().split()
y = input().split()
y1 = input().split()

xN = list(map(int, x))
x1N = list(map(int, x1))
yN = list(map(int, y))
y1N = list(map(int, y1))

hasil1 = xN[0] * yN[0] + xN[1] * y1N[0]
hasil2 = xN[0] * yN[1] + xN[1] * y1N[1]
hasil3 = x1N[0] * yN[0] + x1N[1] * y1N[0]
hasil4 =  x1N[0] * yN[1] + x1N[1] * y1N[1]

print(hasil1, hasil2)
print(hasil3, hasil4)


# hasil = arr1 * arr2
# print(hasil)



