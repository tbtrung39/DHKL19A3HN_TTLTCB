n = input("Nhap chuoi: ")
so = ""
for i in n:
    if i.isdigit():
        so = so + i
print("Chuoi so sau khi xoa:", so)
if so == "":
    print("Khong co so")
else:
    n = int(so)
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong = tong + i
    if tong == n:
        print("Đay la so hoan hao")
    else:
        print("Khong phai so hoan hao")