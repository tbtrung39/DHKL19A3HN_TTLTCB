chuoi = input("Nhập chuỗi: ")
chuoi_so = ""
for ky_tu in chuoi:
    if ky_tu >= '0' and ky_tu <= '9':
        chuoi_so = chuoi_so + ky_tu
print("Chuỗi số:", chuoi_so)
if chuoi_so == "":
    print("Không có số để kiểm tra")
else:
   n = int(chuoi_so)
tong = 0
i = 1
while i < n:
        if n % i == 0:
            tong = tong + i
        i = i + 1
if tong == n:
    print(n, "là số hoàn hảo")
else:
    print(n, "không phải số hoàn hảo")