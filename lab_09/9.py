n = int(input("Nhập một số: "))
def dao_nguoc(n):
    if n < 10:
        print(n, end="")
        return
    else:
        print(n % 10, end="")
        dao_nguoc(n // 10)
print("Số ngược lại là: ", end="")
dao_nguoc(n)
print()
