s = input("Nhập chuỗi: ")
so = ""
for c in s:
    if '0' <= c <= '9':
        so = so + c
print("Chuoi so:", so)
if so != "":
    n = int(so)
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong = tong + i
    if tong == n:
        print("là số hoàn hảo")
    else:
        print("Khong la so hoan hao")
else:
    print("Khong co so")