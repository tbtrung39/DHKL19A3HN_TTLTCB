s = input("Nhập chuỗi: ")
count = sum(1 for char in s if char.isdigit())
print(f"Số lượng ký tự là số: {count}")