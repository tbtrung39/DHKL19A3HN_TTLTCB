
str = input("Nhap mot chuoi gom chu va so: ")
chuoi_moi = ""
for i in str:
    if(i.isdigit()):
        chuoi_moi += i
print("Chuoi sau khi chỉ giu lai các ky tu dạng so:\n", chuoi_moi)
n = int(chuoi_moi)
tong_uoc = 0
for j in range(1, n):
    if(n % j == 0):
        tong_uoc += j
if(tong_uoc == n):
    print(f"{n} la so hoan hao")
else:
    print(f"{n} khong phai la so hoan hao")