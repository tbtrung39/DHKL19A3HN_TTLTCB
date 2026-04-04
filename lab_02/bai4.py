n = int(input("Nhập số nguyên n :"))
n = abs(n)
hang_tram = ( n // 100) % 10
if hang_tram:
    print("hàng trăm của số đó là :",hang_tram)
else :
    print("0")