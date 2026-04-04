tu_so = int(input("Nhập tử số :"))
while True :
    mau_so = int(input("Nhập mẫu số :"))
    if mau_so == 0 :
        print("mẫu số phải khác 0!!!")
    else :
        phan_so = tu_so/mau_so
        break
print("Phân số là :",phan_so) 