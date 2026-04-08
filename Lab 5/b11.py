Str = input("Nhập số nhị phân: ")
dec = 0
i = 0
while i < len(Str):
    dec = dec * 2 + int(Str[i])
    i += 1
print("Số thập phân:", dec)