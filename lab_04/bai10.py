chuoi = input("Nhập vào một số thập phân (ví dụ 324.5): ")
i = 0
kq = ""

while i < len(chuoi):
    if chuoi[i] == '0':
        kq = kq + "không "
    elif chuoi[i] == '1':
        kq = kq + "một "
    elif chuoi[i] == '2':
        kq = kq + "hai "
    elif chuoi[i] == '3':
        kq = kq + "ba "
    elif chuoi[i] == '4':
        kq = kq + "bốn "
    elif chuoi[i] == '5':
        kq = kq + "năm "
    elif chuoi[i] == '6':
        kq = kq + "sáu "
    elif chuoi[i] == '7':
        kq = kq + "bảy "
    elif chuoi[i] == '8':
        kq = kq + "tám "
    elif chuoi[i] == '9':
        kq = kq + "chín "
    elif chuoi[i] == '.':
        kq = kq + "phẩy "
    i = i + 1

print("Chuyển đổi thành dạng ký tự:", kq)