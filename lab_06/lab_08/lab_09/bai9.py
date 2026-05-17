def dao(n):
    if n < 10:
        print(n, end="")
        return
    print(n % 10, end="")
    dao(n // 10)
n = int(input("Nhap n: "))
dao(n)