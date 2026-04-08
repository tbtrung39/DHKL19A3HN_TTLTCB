Str = input("Nhập vào một chuỗi ký tự: ")
dem = 0
for ky_tu in Str:
    if (not ky_tu.isalpha()) and (not ky_tu.isdigit()):
        dem = dem + 1 
print("Số lượng ký tự không phải chữ cái tiếng Anh và không phải số là:", dem)
