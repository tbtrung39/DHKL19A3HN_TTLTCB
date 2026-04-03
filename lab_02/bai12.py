ngay = int(input("Nhap ngay: "))
thang = int(input("Nhap thang (1-12): "))

if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    so_ngay = 31
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    so_ngay = 30
elif thang == 2:
    so_ngay = 28
else:
    so_ngay = 0

if so_ngay == 0 or ngay < 1 or ngay > so_ngay:
    print("ngay thang khong hop le")
else:
    if ngay < so_ngay:
        print("Ngay tiep theo la:", ngay + 1, thang)
    else: 
        if thang == 12:
            print("Ngay tiep theo la: 1/1")
        else:
            print("Ngay tiep theo la: 1/", thang + 1)