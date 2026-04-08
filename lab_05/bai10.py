s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")

res = ""
for i in range(len(s1)):
    for j in range(i + 1, len(s1) + 1):
        substring = s1[i:j]
        if substring in s2 and len(substring) > len(res):
            res = substring

print(f"Chuỗi con chung dài nhất là: '{res}'")