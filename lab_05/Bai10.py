Str1 = input("Nhập chuỗi 1: ")
Str2 = input("Nhập chuỗi 2: ")
max_len = 0
lcs = ""

for i in range(len(Str1)):
    for j in range(i, len(Str1)):
        sub = Str1[i:j+1]
        if sub in Str2 and len(sub) > max_len:
            max_len = len(sub)
            lcs = sub
            
print("Chuỗi con chung dài nhất:", lcs)