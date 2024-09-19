n = int(input('masukkan nilai c: '))
memenuhi = False
for i in range(1,n):
    for j in range (1,n):
        if i**2 + j ** 2 == pow(n,2):
            print("a=",i,"b=",j)
            memenuhi = True

if not memenuhi:
    print("tidak ada pasangan yang memenuhi")


