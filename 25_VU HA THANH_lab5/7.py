chuoi_nhap = input("Nhập chuỗi bất kỳ: ")

chuoi_so = ""
for ky_tu in chuoi_nhap:
    if '0' <= ky_tu <= '9':
        chuoi_so = chuoi_so + ky_tu

print("Chuỗi số thu được là:", chuoi_so)
if chuoi_so != "":
    n = int(chuoi_so)
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong = tong + i
            
    if tong == n and n != 0:
        print(n, "là số hoàn hảo")
    else:
        print(n, "không phải là số hoàn hảo")
else:
    print("Không có số nào trong chuỗi để kiểm tra!")