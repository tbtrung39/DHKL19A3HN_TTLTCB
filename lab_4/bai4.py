tu = int(input("Nhập tử số: "))

while True:  
    mau = int(input("Nhập mẫu số (khác 0): "))
    if mau != 0:
        break
    else:
        print("Mẫu phải khác 0, nhập lại!")

print("Phân số là:", tu, "/", mau)
