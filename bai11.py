n = int(input("Nhập n: "))
if n <= 0:
    print("Không hợp lệ!")
else:
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            if i == 1 or i == n or j == 1 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()