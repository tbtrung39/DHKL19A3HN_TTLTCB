s = input("Nhập chuỗi: ")
so = ""
for c in s:
    if '0' <= c <= '9':
        so += c
print("Chuỗi số:", so)
if so == "":
    print("Không có số")
else:
    n = int(so)
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    if tong == n:
        print("Là số hoàn hảo")
    else:
        print("Không phải số hoàn hảo")