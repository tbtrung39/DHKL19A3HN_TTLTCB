n = int(input("Nhập n: "))
tong = 1
tich = 1
for i in range(n+1):
    tich *= (2*i + 2)/(2*i + 3)
    print(tich)
    tong += tich
print("Đ/A:", tong)