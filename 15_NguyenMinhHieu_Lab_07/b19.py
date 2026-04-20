# a,
n = int(input("Nhập số lượng công nhân hiện có: "))
mnv = []
ttnv = []
for i in range(n):
    print(f"Nhập thông tin của nhân viên thứ {i + 1}:")
    while(True):
        ma_nv = input(f"Nhập mã nhân viên thứ {i + 1}: ")
        if(len(ma_nv) == 4):
            mnv.append(ma_nv)
            break
        else:
            print("Mã nhân viên phải có độ dài là 4!")
    ten_nv = input("Nhập tên nhân viên: ")
    nam_sinh = int(input("Nhập năm sinh: "))
    luong = int(input("Nhập lương: "))
    thong_tin = [ten_nv, nam_sinh, luong]
    ttnv.append(thong_tin)
# b,
m = int(input("Nhập số lượng nhân viên muốn thêm thông tin: "))
for j in range(m):
    print(f"Nhập thông tin của nhân viên thứ {j + 1} muốn thêm vào: ")
    while(True):
        ma_nhanvien = input("Nhập mã nhân viên: ")
        if(len(ma_nv) == 4):
            mnv.append(ma_nhanvien)
            break
        else:
            print("Mã nhân viên phải có độ dài là 4!")
    ten_nv = input("Nhập tên nhân viên: ")
    nam_sinh = int(input("Nhập năm sinh: "))
    luong = int(input("Nhập lương: "))
    thong_tin = [ten_nv, nam_sinh, luong]
    ttnv.append(thong_tin)
danh_sach_nv = dict(zip(mnv, ttnv))
print("Danh sách nhân viên hiện có:")
for tl in danh_sach_nv.items():
    print(tl)
#c, 
vtri_x = []
for i in mnv:
    for j in range(len(i)):
        if(i[j] == "x"):
            vtri_x.append(i)
print("Danh sách nhân viên có giá trị x trong mã nhân viên:")
for k in danh_sach_nv.keys():
    if(k in vtri_x):
        print(danh_sach_nv[k])
#d,
vtri_y = []
for h in mnv:
    for tl in range(len(h)):
        if(h[tl] == "y"):
            vtri_y.append(h)
print("Danh sách nhân viên có giá trị y trong mã nhân viên:")
for k in danh_sach_nv.keys():
    if(k in vtri_y):
        print(danh_sach_nv[k])
        danh_sach_nv[k][2] = danh_sach_nv[k][2] + 1000000
print("Danh sách sau cập nhật!")
for row in danh_sach_nv.items():
    print(row)
#e,
vtri_z = []
for i in mnv:
    for j in range(len(i)):
        if(i[j] == "z"):
            vtri_z.append(i)
print("Danh sách nhân viên có giá trị z trong mã nhân viên:")
for k in danh_sach_nv.keys():
    if(k in vtri_z):
        print(danh_sach_nv[k])
for ii in list(danh_sach_nv.keys()):
    if(ii in vtri_z):
        danh_sach_nv.pop(ii)
print("Danh sách sau khi xoá:")
for i in danh_sach_nv.items():
    print(i)
#f, 
danh_sach_nv = sorted(danh_sach_nv.items(), key=lambda i: i[1][1], reverse=True)
print("Danh sách sau khi sắp xếp:")
danh_sach_nv = dict(danh_sach_nv)
for ttl in danh_sach_nv.items():
    print(ttl)