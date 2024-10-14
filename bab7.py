# acak = input("masukkan kata acak: ")

# pisah = list(map(str, acak))

# i = 0
# while i < len(pisah):    
#     if  i == 0:
#         print(pisah[i].upper(), end="")
#     else:
#         print(pisah[i].lower(), end="")
#     i += 1
# print()  # untuk membuat baris baru

# versi 2
# ack = input("masukkan kata acak: ");
# print(ack[0].upper() + ack[1:].lower())  # untuk membuat bar

rts = [];

for i in range(8):
    print(f"Masukkan angka baris ke-{i+1}: ", end='');
    inp = input();
    inp_int = list(map(int, inp.split(' ')));
    rts.append(inp_int);  

for k in range(8):
    for l in range(8):
        print(rts[7-k][7-l], end=" ");
    print();