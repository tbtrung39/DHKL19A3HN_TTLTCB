n = int(input("Nhap so nguyen: "))
if n == 0:
    print("So nhi phan: 0")
else:
    np = ""
    while n > 0:
        np = str(n % 2) + np
        n //= 2
    print("So nhi phan:", np)