n = int(input("nhap n:"))
#a
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#b
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(i):
        print("* ", end="")
    print()
#c
for i in range(1, n + 1):
    # in khoảng trắng
    for j in range(n - i):
        print(" ", end="")
    # in dấu *
    for j in range(2 * i - 1):
        print("*", end="")
    print()