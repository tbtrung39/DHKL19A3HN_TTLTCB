tu_so = int(input("Nhap tu so: "))

while True:
    mau_so = int(input("Nhap mau so: "))
    if mau_so != 0:
        break
    print("Nhap lai mau so khac 0")
print("Ket qua la: ", tu_so / mau_so)