# lst = [2,4,6,7,8];
# lst2 = [];

# def tambah(ll):
#     for i in ll:
#         lst2.append(i+2);
#     print(lst2);

# tambah(lst)
    
lstr1 = [123,2714,902,990,364,274];


def bubbleShort(lstr):
    for i in range(len(lstr) - 1):
        for j in  range(len(lstr) - 1 - i):
            if lstr[j] > lstr[j + 1]:
                temp = lstr[j];
                lstr[j] = lstr[j+1];
                lstr[j + 1] = temp;
    return lstr1;

print(bubbleShort(lstr1));

        