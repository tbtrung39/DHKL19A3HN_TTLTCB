def dao_nguoc(n, rev=0):
    if n == 0:
        return rev
    return dao_nguoc(n // 10, rev * 10 + n % 10)
n = int(input("Nhập số: "))
print("Số đảo ngược là:", dao_nguoc(n))