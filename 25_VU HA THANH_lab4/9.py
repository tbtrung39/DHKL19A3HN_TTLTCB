# Bước 1: Nhập số từ bàn phím (để dạng chuỗi để dễ duyệt từng chữ số)
n = input("Nhập vào một số nguyên: ")

# Bước 2: Dùng vòng lặp để cộng dồn từng chữ số
tong = 0
for chu_so in n:
    # Kiểm tra nếu là số thì mới cộng (phòng trường hợp người dùng nhập dấu trừ hoặc chữ)
    if chu_so.isdigit():
        tong += int(chu_so)

# Bước 3: In kết quả
print(f"Tổng các chữ số của {n} là: {tong}")