print("""
--- MENU ---
1. Cafe
2. Cam vắt
3. Nước ép cà rốt
4. Nước lọc
5. Nước dừa
""")

chon = int(input("Mời bạn chọn đồ uống (1-5): "))

if chon == 1: print("Bạn đã chọn Cafe.")
elif chon == 2: print("Bạn đã chọn Cam vắt.")
elif chon == 3: print("Bạn đã chọn Nước ép cà rốt.")
elif chon == 4: print("Bạn đã chọn Nước lọc.")
elif chon == 5: print("Bạn đã chọn Nước dừa.")
else: print("Món này không có trong menu!")