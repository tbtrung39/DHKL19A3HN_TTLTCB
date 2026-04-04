s = input("Nhập chuỗi: ")
max_sub = ""
temp = ""
i = 0
while i < len(s):
    if i == 0 or s[i] == s[i-1]:
        temp = temp + s[i]
    else:
        if len(temp) > len(max_sub):
            max_sub = temp
        temp = s[i]
    i = i + 1
if len(temp) > len(max_sub):
    max_sub = temp
print("Chuỗi con dài nhất:", max_sub)