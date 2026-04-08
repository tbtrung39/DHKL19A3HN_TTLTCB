s = input("Nhập chuỗi: ")
count = 0
for char in s:
    if not char.isalnum(): 
        count += 1
print(f"Số lượng ký tự đặc biệt: {count}")