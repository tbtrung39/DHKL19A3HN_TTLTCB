tu_so = int(input("Nhập tử số: "))

while True:
    mau_so = int(input("Nhập mẫu số: "))
    if mau_so != 0:
        break
    print("Nhập lại mẫu số phải khác 0 ")

print("Kết quả là: ", tu_so / mau_so)