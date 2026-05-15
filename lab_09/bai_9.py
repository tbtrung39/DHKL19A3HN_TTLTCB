n = int(input("Nhap mot so: "))
def dao_nguoc(n):
    if n < 10:
        print(n, end="")
        return
    else:
        print(n % 10, end="")
        dao_nguoc(n // 10)
print("So nguoc lai la: ", end="")
dao_nguoc(n)
print()