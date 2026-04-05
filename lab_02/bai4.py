n = int(input("Nhập n:"))
if n < 0:
    print("Số này có 2 chữ số không có hàng trăm")
else:
    tram = (n // 100)%10
    print("hàng trăm của",n,"là:",tram)