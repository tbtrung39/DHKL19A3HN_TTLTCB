str = input("Nhap chuoi ky tu: ")
so_str = ""
for ch in str:
    if ch.isdigit():
        so_str += ch         #ch.isdigit():kiểm tra có phải số k
print("Chuoi so:", so_str)

if so_str != "":
    n = int(so_str)
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    if tong == n:
        print("La so hoan hao")
    else:
        print("Khong phai so hoan hao")