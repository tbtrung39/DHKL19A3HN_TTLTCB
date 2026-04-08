n = int(input("Nhập n: "))
tong = sum(1/i for i in range(1, n + 1))
print(f"Tổng nghịch đảo: {round(tong, 3)}")