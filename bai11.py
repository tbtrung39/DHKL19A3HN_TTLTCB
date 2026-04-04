s = input("Nhập chuỗi nhị phân: ")
decimal = 0
i = 0
while i < len(s):
    decimal = decimal * 2 + (ord(s[i]) - ord('0'))
    i += 1
print("Hệ thập phân:", decimal)