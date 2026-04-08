import math

# 1. Nhập dữ liệu
x = float(input("Nhập giá trị x (radian): "))
sai_so_cho_phep = 0.0001 # Tương đương 10^-4

# 2. Khởi tạo các giá trị ban đầu
cos_x = 1.0    # Số hạng đầu tiên trong dãy Taylor là 1
so_hang = 1.0  # Biến lưu giá trị của từng số hạng để so sánh với sai số
k = 1          # Biến đếm (tương ứng với k trong công thức tổng quát)

# 3. Vòng lặp tính toán
# Tiếp tục cộng nếu số hạng tiếp theo vẫn còn lớn hơn sai số cho phép
while abs(so_hang) >= sai_so_cho_phep:
    # Công thức tổng quát của số hạng thứ k:
    # (-1)^k * x^(2k) / (2k)!
    
    # Tính tử số và mẫu số của số hạng thứ k
    tu_so = ((-1)**k) * (x**(2*k))
    mau_so = math.factorial(2*k)
    
    so_hang = tu_so / mau_so
    cos_x += so_hang
    k += 1

# 4. In kết quả
print(f"Giá trị cos({x}) tính bằng Taylor: {cos_x}")
print(f"Giá trị cos({x}) tính bằng thư viện math: {math.cos(x)}")