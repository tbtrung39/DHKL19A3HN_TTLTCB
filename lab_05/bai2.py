str = input("Nhập chuỗi kí tự :")
dem = 0
for ky_tu in str :
    if not ('a' <= ky_tu <='z' or 'A' <= ky_tu <= 'Z') and not '0'<= ky_tu <= '9':
        dem += 1
print("ký tự không phải là chữ cái tiếng anh và không phải là số là :",dem)