Str = input("Nhập vào 1 chuỗi số kí tự :")
dem = 0
for ky_tu in Str:
    if "0"<=ky_tu<="9":
        dem += 1
print("số các ký tự là số trong chuỗi đã nhập : ",dem)