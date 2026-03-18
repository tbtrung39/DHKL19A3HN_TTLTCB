'''4. Nhập vào 1 số nguyên, yêu cầu xuất ra chữ số hàng trăm của số đó, nếu không có thì xuất ra 0.'''

n = int(input("Nhập số nguyên: "))
if n < 100 and n > -100:
    print("Xuất ra 0")
else:
    if n >= 0:
        hang_tram = (n // 100) % 10
    else:
        hang_tram = ((-n) // 100) % 10   
    print("Chữ số hàng trăm là:", hang_tram)