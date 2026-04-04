chuoi = input("Nhap chuoi str: ")
dem = 0
for ky_tu in chuoi:
    if ky_tu.isdigit():
        dem += 1
print(f"So luong ki tu la so trong chuoi: {dem}")