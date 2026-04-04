n = int(input("Nhập vào một số nguyên: "))
print(f"Số nguyên được nhập vào là: {n}")
if((n >= 100) or (n <= -100)):
    n = str(n)
    print(f"Chữ số hàng trăm của {n} là: {n[-3]}")
else:
    print(0)