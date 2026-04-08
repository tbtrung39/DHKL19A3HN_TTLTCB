n = int(input("Nhập n: "))
tong = 1.0
temp = 1.0
for i in range(1, n + 1):
    temp *= (2 * i) / (2 * i + 1)
    tong += temp
print(f"Kết quả: {round(tong, 3)}")