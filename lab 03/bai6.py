n = int(input("Nhập n: "))
tong = sum(i**3 for i in range(1, n + 1))
print(f"Tổng bậc 3: {tong}")