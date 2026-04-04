chon = 0
while chon < 1 or chon > 5:
    print("--- MENU ĐỒ UỐNG ---")
    print("1. Cafe")
    print("2. Cam vắt")
    print("3. Nước ép cà rốt")
    print("4. Nước lọc")
    print("5. Nước dừa")
    chon = int(input("Mời bạn chọn đồ uống (nhập số từ 1 đến 5): "))
    
    if chon == 1:
        print("Bạn đã gọi: Cafe")
    elif chon == 2:
        print("Bạn đã gọi: Cam vắt")
    elif chon == 3:
        print("Bạn đã gọi: Nước ép cà rốt")
    elif chon == 4:
        print("Bạn đã gọi: Nước lọc")
    elif chon == 5:
        print("Bạn đã gọi: Nước dừa")
    else:
        print("Lựa chọn không có trong menu, vui lòng nhập lại!")