d = {}

while True:
    print("\n1. Thêm nhân viên")
    print("2. Tìm kiếm nhân viên")
    print("3. Tăng lương")
    print("4. Xóa nhân viên")
    print("5. Sắp xếp theo năm sinh")
    print("6. In danh sách")
    print("7. Thoát")
    
    chon = input("Nhập lựa chọn (1-7): ")
    
    if chon == "1":
        ma_nv = input("Nhập mã nhân viên (4 ký tự): ")
        ho_ten = input("Nhập họ tên (20 ký tự): ")
        nam_sinh = int(input("Nhập năm sinh: "))
        luong = int(input("Nhập lương: "))
        
        d[ma_nv] = {"ho_ten": ho_ten, "nam_sinh": nam_sinh, "luong": luong}
        print("Thêm nhân viên thành công")
    
    elif chon == "2":
        x = input("Nhập mã nhân viên cần tìm: ")
        if x in d:
            print("Mã NV: " + x)
            print("Họ tên: " + d[x]["ho_ten"])
            print("Năm sinh: " + str(d[x]["nam_sinh"]))
            print("Lương: " + str(d[x]["luong"]))
        else:
            print("Không tìm thấy nhân viên")
    
    elif chon == "3":
        y = input("Nhập mã nhân viên cần tăng lương: ")
        if y in d:
            d[y]["luong"] = d[y]["luong"] + 1000000
            print("Tăng lương thành công")
        else:
            print("Không tìm thấy nhân viên")
    
    elif chon == "4":
        z = input("Nhập mã nhân viên cần xóa: ")
        if z in d:
            del d[z]
            print("Xóa nhân viên thành công")
        else:
            print("Không tìm thấy nhân viên")
    
    elif chon == "5":
        sorted_d = sorted(d.items(), key=lambda x: x[1]["nam_sinh"], reverse=True)
        print("Danh sách sắp xếp giảm dần theo năm sinh:")
        for ma_nv, info in sorted_d:
            print("Mã: " + ma_nv + " - Tên: " + info["ho_ten"] + " - Năm: " + str(info["nam_sinh"]) + " - Lương: " + str(info["luong"]))
    
    elif chon == "6":
        print("Danh sách nhân viên:")
        for ma_nv in d:
            print("Mã: " + ma_nv + " - Tên: " + d[ma_nv]["ho_ten"] + " - Năm: " + str(d[ma_nv]["nam_sinh"]) + " - Lương: " + str(d[ma_nv]["luong"]))
    
    elif chon == "7":
        break
