def nhap_thong_tin():
    while(True):
        ten = input("Nhập tên nhân viên: ")
        que_quan = input("Quê quán: ")
        tnct = int(input("Thâm niên công tác (năm): "))
        if(tnct < 0):
            print("Thâm niên công tác không hợp lệ, vui lòng nhập lại!")
        else:
            break
    return ten, que_quan, tnct
ho_ten, que_quan, tnct = nhap_thong_tin()
def tinh_luong():
    if(tnct > 2 and tnct < 5):
        luong = 7000000
    if(tnct >= 5 and tnct < 10):
        luong = 10000000
    else:
        luong = 15000000
    return luong
luong_cb = tinh_luong()
def hien_thong_tin():
    thong_tin = {
        "Họ tên": ho_ten,
        "Quê quán": que_quan,
        "Thâm niên công tác": tnct,
        "Lương cơ bản": luong_cb
    }
    return thong_tin
thong_tin = hien_thong_tin()
for i in thong_tin.items():
    print(i)