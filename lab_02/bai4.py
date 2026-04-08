n = int(input("Nhập vào một số nguyên: "))
chu_so_hang_tram = (abs(n) // 100) % 10

if abs(n) < 100:
    print("0")
else:
    print(f"Chữ số hàng trăm là: {chu_so_hang_tram}")