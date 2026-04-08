Str = input("Nhập chuỗi: ")
max_str = ""
temp = Str[0]
i = 1
while i < len(Str):
    if Str[i] == Str[i-1]:
        temp += Str[i]
    else:
        if len(temp) > len(max_str):
            max_str = temp
        temp = Str[i]
    i += 1
if len(temp) > len(max_str):
    max_str = temp
print("Chuỗi con dài nhất:", max_str)