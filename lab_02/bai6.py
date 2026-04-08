n = int(input("Nhập số 3 chữ số: "))

tram = n // 100
chuc = (n // 10) % 10
donvi = n % 10

print("Hàng trăm:", tram)
print("Hàng chục:", chuc)
print("Hàng đơn vị:", donvi)