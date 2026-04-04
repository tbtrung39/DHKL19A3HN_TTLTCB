
str = input("Nhập một chuỗi gồm chữ và số: ")
chuoi_moi = ""
for i in str:
    if(i.isdigit()):
        chuoi_moi += i
print("Chuỗi sau khi chỉ giữ lại các ký tự dạng số:\n", chuoi_moi)
n = int(chuoi_moi)
tong_uoc = 0
for j in range(1, n):
    if(n % j == 0):
        tong_uoc += j
if(tong_uoc == n):
    print(f"{n} là số hoàn hảo!")
else:
    print(f"{n} không phải là số hoàn hảo!")
