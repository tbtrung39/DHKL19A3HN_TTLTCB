n = int(input("Nhap n (>0): "))
while n <= 0:
    n = int(input("Nhap lai n > 0: "))
print("Phan tich:", end=" ")
for i in range(2, n+1):
    while n % i == 0:
        print(i, end=" ")
        n = n // i