n = int(input("Nhập số nguyên :"))
if n < 100 or n > 999 :
    print(" phải in ra số nguyên có 3 chữ số")
    n = int(input("Nhập lại số nguyên"))
else :
    tram = n // 100
    chuc = ( n // 10) % 10
    don_vi = n % 10
    so = ['không','một','hai','ba','bốn','năm','sáu','bảy','tám','chín']
    print(so[tram],"trăm",end = " ")
    if chuc == 0 :
        print("linh",end = " ")
    elif chuc == 1:
        print("mười",end = " ")
    else :
        print(so[chuc],"mươi",end =" ")
    if don_vi == 5 and chuc != 0:
        print("lăm",end= " ")
    elif don_vi == 1 and chuc ==[0,1] :
        print("mốt",end = " ")
    else :
        print(so[don_vi],end = " ")
