tu = int(input("nhập tử: "))
mau = int(input("nhập mẫu: "))
while mau <= 0:
    mau = int(input("Vui lòng nhập lại (mẫu > 0): "))
print("Phân số bạn vừa nhập là: ",tu,"/",mau)