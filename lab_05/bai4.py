s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
result = ""
i, j = 0, 0
while i < len(s1) or j < len(s2):
    if i < len(s1):
        result += s1[i]
        i += 1
    if j < len(s2):
        result += s2[j]
        j += 1
print(f"Chuỗi sau khi trộn: {result}")