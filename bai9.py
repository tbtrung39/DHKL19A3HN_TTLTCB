n = int(input("Nhập n (n > 0): "))

if n <= 0:
    print("n không hợp lệ!")
else:
    S4 = 0
    for i in range(1, n + 1):
        S4 += i**2

    S5 = 0
    for i in range(n + 1):
        S5 += (2*i + 1)**3

    S6 = 0
    for i in range(1, n + 1):
        S6 += (2*i)**4

    print("S4 =", S4)
    print("S5 =", S5)
    print("S6 =", S6)