n = int(input("Nhập n: "))
S = 1.0
a = 1.0
for i in range(1, n + 2):
    a = a * (2 * i) / (2 * i + 1)
    S += a
print(f"Kết quả: {round(S, 3)}")