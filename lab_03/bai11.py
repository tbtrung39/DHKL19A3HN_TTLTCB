n = int(input("Nhập n: "))
for i in range(1, n + 1):
    for j in range(1, 2*n):
        if j == n - i + 1 or j == n + i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n = int(input("Nhập n: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n = int(input("Nhập n: "))
for i in range(1, n + 1):
    for j in range(1, 2*n):
        if n - i + 1 <= j <= n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()