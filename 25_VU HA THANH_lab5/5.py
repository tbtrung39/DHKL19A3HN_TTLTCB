# Bước 1: Nhập chuỗi
s = input("Nhập vào chuỗi Str: ")
chuoi_so = ""
for ky_tu in s:
    if '0' <= ky_tu <= '9':
        chuoi_so = chuoi_so + ky_tu
if chuoi_so == "":
    print("Chuỗi sau khi lọc không có số nào.")
else:
    print("Chuỗi số còn lại là:", chuoi_so)
    
    n = int(chuoi_so)
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc = tong_uoc + i
    if tong_uoc == n and n != 0:
        print("Thông báo: Đây là số hoàn hảo.")
    else:
        print("Thông báo: Đây không phải là số hoàn hảo.")