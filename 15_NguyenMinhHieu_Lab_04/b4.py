tu_so = float(input("Nhập tử số: "))
mau_so = float(input("Nhập mẫu số: "))
while(True):
    if(mau_so != 0):
        print(tu_so, "/", mau_so)
        break
    else:
        print("Mẫu số phải khác 0, nhập lại!")
        while(mau_so == 0):
            mau_so = float(input("Nhập mẫu số: "))
            if(mau_so == 0):
                print("Mẫu số phải khác 0, nhập lại!")
        print(tu_so, "/", mau_so)
        break