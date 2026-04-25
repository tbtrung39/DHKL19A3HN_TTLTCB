def nam_nhuan(x):
    if(x % 4 == 0 and x % 100 != 0 or x % 400 == 0):
        return True
    else:
        return False
y = int(input("Nhập năm để kiểm tra: "))
if(nam_nhuan(y)):
    print(f"{y} là năm nhuận!")
else:
    print(f"{y} không phải là năm nhuận!")
while(True):
    m = int(input("Nhập tháng để kiểm tra: "))
    if(m > 12 or m < 0):
        print("Tháng không hợp lệ, nhập lại!")
    else:
        break
def kiem_tra_thang(i):
    if(nam_nhuan(y)):
        if(i in [1, 3, 5, 7, 8, 10, 12]):
            print(f"Tháng {i}, năm {y} có 31 ngày!")
        elif(i == 2):
            print(f"Tháng {i}, năm {y} có 29 ngày!")
        else:
            print(f"Tháng {i} năm {y} có 30 ngày!")
    else:
        if(i in [1, 3, 5, 7, 8, 10, 12]):
            print(f"Tháng {i}, năm {y} có 31 ngày!")
        elif(i == 2):
            print(f"Tháng {i}, năm {y} có 28 ngày!")
        else:
            print(f"Tháng {i} năm {y} có 30 ngày!")
    return True
kiem_tra_thang(m)