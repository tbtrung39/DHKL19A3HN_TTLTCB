n = int(input("Nhập vào một số nguyên dương: "))
tong = 0
tam = n

while tam > 0:
    tong = tong + (tam % 10)
    tam = tam // 10

print("Tổng các chữ số của số vừa nhập là:", tong)