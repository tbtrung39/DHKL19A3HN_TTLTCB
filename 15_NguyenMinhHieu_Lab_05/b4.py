chuoi_1 = input("Nhập chuỗi thứ nhất: ")
chuoi_2 = input("Nhập chuỗi thứ hai: ")
chuoi_dan = ""
chuoi_lien = ""
print("Chuỗi liền:")
for i in chuoi_1:
    chuoi_lien += i
for j in chuoi_2:
    chuoi_lien += j
print(chuoi_lien)
print("Chuỗi đan:")
x = 0
while(x != 1):
    for i, j in zip(chuoi_1,chuoi_2):
        chuoi_dan += i
        chuoi_dan += j
    do_dai_min = min(len(chuoi_1), len(chuoi_2))
    print(chuoi_1[do_dai_min:])
    print(chuoi_2[do_dai_min:])
    chuoi_dan += chuoi_1[do_dai_min:] 
    chuoi_dan += chuoi_2[do_dai_min:]
    x += 1
print(chuoi_dan)