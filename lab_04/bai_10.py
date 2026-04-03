n = int(input("Nhap n: "))

if n < 2:
    print("Khong phai so nguyen to")
else:
    i = 2
    la_snt = True

    while i <= n // 2:
        if n % i == 0:
            la_snt = False
            break
        i = i + 1

    if la_snt:
        print("La so nguyen to")
    else:
        print("Khong phai so nguyen to")