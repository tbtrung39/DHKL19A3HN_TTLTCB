d = {}

n = int(input("Nhập số thí sinh: "))

for i in range(n):
    so_bao_danh = input("Nhập số báo danh: ")
    ho_ten = input("Nhập họ và tên: ")
    diem = float(input("Nhập điểm thi: "))
    
    d[so_bao_danh] = {"ho_ten": ho_ten, "diem": diem}

so_bao_danh_tim = input("\nNhập số báo danh cần tìm: ")

if so_bao_danh_tim in d:
    print("Họ và tên: " + d[so_bao_danh_tim]["ho_ten"])
    print("Điểm thi: " + str(d[so_bao_danh_tim]["diem"]))
else:
    print("Không tìm thấy thí sinh có số báo danh: " + so_bao_danh_tim)
