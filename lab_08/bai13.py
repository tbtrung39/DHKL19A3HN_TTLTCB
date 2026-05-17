def la_nam_nhuan(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def so_ngay_thang(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if la_nam_nhuan(year):
            return 29
        else:
            return 28
    else:
        return -1

month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

if month < 1 or month > 12:
    print("Tháng không hợp lệ!")
else:
    nam_nhuan = la_nam_nhuan(year)
    so_ngay = so_ngay_thang(month, year)
    
    print(f"Tháng {month} năm {year}:")
    if nam_nhuan:
        print(f"Năm {year} là năm nhuận")
    else:
        print(f"Năm {year} không phải năm nhuận")
    print(f"Số ngày: {so_ngay}")
