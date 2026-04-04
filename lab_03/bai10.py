n = int(input("Nhap so nguyen duong n: "))

print("Phan tich:", end=" ")

for i in range(2, n + 1):
    for _ in range(n):   
        if n % i == 0:
            print(i, end=" ")
            n = n // i
        else:
            break