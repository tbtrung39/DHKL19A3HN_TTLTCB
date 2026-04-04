str = input("Nhap chuoi ky tu: ")
dem = 0
for ch in str:
    if not ch.isalpha() and not ch.isdigit():  #ch.isalpha(): kiểm tra có phải chữ cái khong
        dem += 1                               #ch.isdigit():kiểm tra có phải số khong
print("So ky tu dac biet:", dem)