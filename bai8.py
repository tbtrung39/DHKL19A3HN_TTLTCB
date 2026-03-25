n = int(input("Nhập n (n > 0): "))

if n <= 0:
    print("n không hợp lệ!")
else:
    S1 = 0
    for i in range(1, n + 1):
        S1 += i

    S2 = 0
    for i in range(n + 1):
        S2 += 2*i + 1

    S3 = 0
    for i in range(1, n + 1):
        S3 += 2*i

    print("S1 =", S1)
    print("S2 =", S2)
    print("S3 =", S3)