s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
max_str = ""
i = 0
while i < len(s1):
    j = i + 1
    while j <= len(s1):
        sub = s1[i:j]
        if sub in s2 and len(sub) > len(max_str):
            max_str = sub
        j += 1
    i += 1
print("Chuỗi chung dài nhất:", max_str)