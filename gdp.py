s = '1001'
sN = list(map(int, s))
j1 = sN[3]
j2 = sN[2]
j3 = sN[1]
j4 = sN[0]

J1 = pow(2,0) * j1
J2 = pow(2,1) * j2
J3 = pow(2,2) * j3
J4 = pow(2,3) * j4
hasil = J1 + J2 + J3 + J4
print(hasil)
