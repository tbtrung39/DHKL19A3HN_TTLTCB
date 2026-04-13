Ds = []
while(True):
    chuc_nang = input("Nhập tên chức năng (D: Tiền gửi; W: Tiền rút; 0: Để thoát): ")
    chuc_nang = chuc_nang.upper()
    if(chuc_nang == "D"):
        d = int(input("Nhập số tiền cần gửi: "))
        Ds.append(d)
    elif(chuc_nang == "W"):
        w = int(input("Nhập số tiền cần rút: "))
        Ds.append(-w)
    elif(chuc_nang == "0"):
        print("Tạm biệt!")
        break
    else:
        print("Chỉ có 3 chức năng! Vui lòng nhập lại!")
print(Ds)
print(f"Số tiền còn lại là: {sum(Ds)}")