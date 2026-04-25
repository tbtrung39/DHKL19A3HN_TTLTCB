def nhap_thong_tin():
    while(True):
        ten = input("Nhập tên học sinh: ")
        toan = float(input("Nhập điểm toán: "))
        ly = float(input("Nhập điểm lý: "))
        hoa = float(input("Nhập điểm hoá: "))
        if(toan > 10 or toan < 0 or ly < 0 or ly > 10 or hoa > 10 or hoa < 0):
            print("Nhập lại điểm!")
        else:
            break
    return ten, toan, ly, hoa
ten, toan, ly, hoa = nhap_thong_tin()
def hien_thong_tin():
    thong_tin = {
        "Họ Tên": ten,
        "Điểm toán": toan,
        "Điểm lý": ly,
        "Điểm hoá": hoa
    }
    return thong_tin
thong_tin = hien_thong_tin()
def tinh_trung_binh():
    return (toan + ly + hoa)/3
diem_tb = tinh_trung_binh()
print("Thông tin:")
for row in thong_tin.items():
    print(row)
print(diem_tb)