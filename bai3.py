n = int(input("Nhập số n: "))
kq = ""
if n == 0:
    kq = "0"
while n > 0:
    kq = str(n % 2) + kq
    n = n // 2
print("Số nhị phân:", kq)