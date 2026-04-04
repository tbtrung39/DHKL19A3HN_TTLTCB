s = input("Nhập chuỗi: ")
temp = ""
i = 0
s = s + " "
while i < len(s):
    if s[i] != " " and s[i] != ",":
        temp += s[i]
    else:
        if temp != "":
            print(temp)
        temp = ""
    i += 1