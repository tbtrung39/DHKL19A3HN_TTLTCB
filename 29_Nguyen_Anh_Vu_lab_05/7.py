str = input("Nhập một chuỗi gồm chữ và số: ")
ky_tu_so = ""
for i in str:
    if(i.isdigit()):
        ky_tu_so += i
print("Chuỗi sau khi lọc:", ky_tu_so)
n = int(ky_tu_so)
tong_uoc = 0
for i in range(1, n):
    if(n % i == 0):
        tong_uoc += i
if(tong_uoc == n):
    print(f"{n} là số hoàn hảo!")
else:
    print(f"{n} không phải là số hoàn hảo!")