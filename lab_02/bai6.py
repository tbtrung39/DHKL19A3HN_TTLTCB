so = int(input("Nhap so nguyen: "))
if 100 <= abs(so) <= 999:
    a = abs(so)
    hangtram = a // 100
    hangchuc = (a// 10) % 10
    hangdonvi = a % 10\
    
if hangtram == 1: h = "mot"
elif hangtram == 2: h = "hai"
elif hangtram == 3: h = "ba"
elif hangtram == 4: h = "bon"
elif hangtram == 5: h = "nam"
elif hangtram == 6: h = "sau"
elif hangtram == 7: h = "bay"
elif hangtram == 8: h = "tam"
elif hangtram == 9: h = "chin"

if hangchuc == 1: c = "mot"
elif hangchuc == 2: c = "hai"
elif hangchuc == 3: c = "ba"
elif hangchuc == 4: c = "bon"
elif hangchuc == 5: c = "nam"
elif hangchuc == 6: c = "sau"
elif hangchuc == 7: c = "bay"
elif hangchuc == 8: c = "tam"
elif hangchuc == 9: c = "chin"

if hangdonvi == 1: d = "mot"
elif hangdonvi == 2: d = "hai"
elif hangdonvi == 3: d = "ba"
elif hangdonvi == 4: d = "bon"
elif hangdonvi == 5: d = "nam"
elif hangdonvi == 6: d = "sau"
elif hangdonvi == 7: d = "bay"
elif hangdonvi == 8: d = "tam"
elif hangdonvi == 9: d = "chin"
else:
    print("So nhap khong hop le")

print("Cach doc:", h, "tram", c, "muoii", d)

