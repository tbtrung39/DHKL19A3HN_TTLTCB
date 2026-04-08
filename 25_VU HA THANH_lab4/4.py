# 1. Nhập tử số
tu_so = float(input("Nhập tử số: "))

# 2. Nhập mẫu số và kiểm tra điều kiện
while True:
    mau_so = float(input("Nhập mẫu số: "))
    
    if mau_so != 0:
        break  # Nếu mẫu số khác 0 thì thoát vòng lặp
    else:
        print("Mẫu số không được bằng 0. Vui lòng nhập lại!")

# 3. In phân số hoặc kết quả phép chia
print(f"Phân số vừa nhập là: {tu_so}/{mau_so}")
print(f"Giá trị của phân số là: {tu_so / mau_so}")