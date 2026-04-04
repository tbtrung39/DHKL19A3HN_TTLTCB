str = input("Nhap chuoi nhi phan: ")
sothapphan = 0
somu = 0
for i in range(len(str) - 1, -1, -1):
    sothapphan += int(str[i]) * (2 ** somu)
    somu += 1
print("So thap phan:", sothapphan)