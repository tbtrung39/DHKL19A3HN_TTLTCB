
dict_so = {
    '0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn',
    '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín'
}

n = input("Nhập vào một số: ")

danh_sach_chu = [dict_so[ky_tu] for ky_tu in n if ky_tu in dict_so]

print("Kết quả đọc là:", " ".join(danh_sach_chu))