str = input("Nhap chuoi gom ca chu va so: ")
ky_tu_so = ""
for i in str:
    if(i.isdigit()):
        ky_tu_so += i
print("Chuoi sau khi loc:", ky_tu_so)
n = int(ky_tu_so)
tong_uoc = 0
for i in range(1, n):
    if(n % i == 0):
        tong_uoc += i
if(tong_uoc == n):
    print(f"{n} la so hoan hao")
else:
    print(f"{n} khong la so hoan hao")