n = int(input("Nhập số nguyên n: "))
while n <= 0:
    n = int(input("Nhập lại n > 0: "))
tong = 0
for i in range(1,n + 1):
    tong += 1/i
print(f"Phép toán được tính là:{tong}")