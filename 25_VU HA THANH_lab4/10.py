# Bước 1: Định nghĩa bảng từ điển để ánh xạ ký tự sang chữ
bang_chu = {
    '0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn',
    '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín',
    '.': 'chấm', '-': 'âm'
}

# Bước 2: Nhập số (để dạng chuỗi để giữ nguyên dấu chấm thập phân)
n = input("Nhập vào một số thập phân: ")

# Bước 3: Duyệt qua từng ký tự và chuyển đổi
ket_qua = []
for ky_tu in n:
    if ky_tu in bang_chu:
        ket_qua.append(bang_chu[ky_tu])

# Bước 4: In kết quả ra màn hình, nối các chữ bằng khoảng trắng
print("Kết quả chuyển đổi:", " ".join(ket_qua))