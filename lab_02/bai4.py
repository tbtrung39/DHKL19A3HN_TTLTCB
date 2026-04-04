n = int(input("Nhập vào một số nguyên: "))

if n < 0:
    n = -n

if n < 100:
    print("Chữ số hàng trăm của số này là: 0")
else:
    print("Chữ số hàng trăm của số này là:", (n // 100) % 10)