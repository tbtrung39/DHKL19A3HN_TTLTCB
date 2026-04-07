n = int(input("Nhập n: "))
tong = 1.0
tich = 1.0
for i in range(1, n + 1):
    tich *= (2 * i) / (2 * i + 1)
    tong += tich
print(f"Kết quả: {round(tong, 3)}")