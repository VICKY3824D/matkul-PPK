# a = 5 
# for i in range(1,a):
#     for j in range (1,i+1):
#         print("i=",i,"j=",j,end=" ")
#     print()

# for i in range(5,15,3):
#     print(i) 
    
# for j in range(17,4,-2):
#     print(j) 
    
# n = int(input())
# for i in range (n,0,-2):
#     print(i)
#     if(i) == 3:
#         break

# a = int(input())
# b = int(input()) 

# while a%b != 0:
#     temp = b
#     b=a
#     a=temp%a

# Input nilai n dari pengguna
n = int(input("Masukkan nilai n (2 ≤ n ≤ 100): "))

# Memproses bilangan dari 2 sampai n
for i in range(2, n + 1):
    prima = True  # Asumsikan i adalah prima
    
    # Memeriksa apakah i adalah bilangan prima
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            prima = False
            break  # Jika ditemukan pembagi, i bukan prima
    
    # Tampilkan hasilnya
    if prima:
        print(i, end=" ")  # Tampilkan bilangan prima
    else:
        print("#", end=" ")  # Tampilkan simbol '#' untuk bilangan bukan prima


        
