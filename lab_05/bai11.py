binary_str = input("Nhập chuỗi nhị phân: ")
try:
    decimal_val = int(binary_str, 2)
    print(f"Giá trị thập phân là: {decimal_val}")
except ValueError:
    print("Chuỗi nhập vào không phải hệ nhị phân hợp lệ!")