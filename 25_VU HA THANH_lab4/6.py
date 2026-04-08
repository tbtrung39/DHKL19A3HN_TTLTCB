# Bước 1: Tạo một danh sách (hoặc từ điển) các chữ số bằng chữ
chu_so = {
    '0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn',
    '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín'
}

# Bước 2: Nhập số từ bàn phím (để nguyên dạng chuỗi để dễ xử lý từng ký tự)
n = input("Nhập vào một số: ")

# Bước 3: Duyệt qua từng ký tự trong chuỗi n và in ra chữ tương ứng
print("Kết quả in ra là:", end=" ")
for ky_tu in n:
    if ky_tu in chu_so:
        print(chu_so[ky_tu], end=" ")