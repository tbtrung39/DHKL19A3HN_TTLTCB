# Bước 1: Nhập một ký tự từ bàn phím
ky_tu = input("Nhập vào một ký tự: ")

# Bước 2: Kiểm tra nếu người dùng nhập nhiều hơn 1 ký tự thì chỉ lấy ký tự đầu tiên
# Hoặc báo lỗi tùy bạn, nhưng hàm ord() chỉ nhận đúng 1 ký tự.
if len(ky_tu) == 1:
    # Bước 3: Sử dụng hàm ord() để lấy mã ASCII
    ma_ascii = ord(ky_tu)
    print(f"Giá trị ASCII của ký tự '{ky_tu}' là: {ma_ascii}")
else:
    print("Vui lòng chỉ nhập đúng một ký tự!")