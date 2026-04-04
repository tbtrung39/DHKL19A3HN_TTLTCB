
chuoi_1 = input("Nhập chuỗi ký tự 1: ")
chuoi_2 = input("Nhập chuỗi ký tự 2: ")
chuoi_con = ""
for i in chuoi_1:
    if(i in chuoi_2):
        chuoi_con += i
        chuoi_2 = chuoi_2.replace(i, "", 1)
print(f"Chuỗi các ký tự con chung: {chuoi_con}")
chuoi_cuoi = ""
kt_str = ""
i = 0
while(i < len(chuoi_con)):
    if(chuoi_con[i] == chuoi_con[i - 1]):
        kt_str += chuoi_con[i]
    else:
        if(len(kt_str) > len(chuoi_cuoi)):
            chuoi_cuoi = kt_str
        kt_str = chuoi_con[i]
    i += 1
if(len(kt_str) > len(chuoi_cuoi)):
    chuoi_cuoi = kt_str
print(f"Chuỗi có độ dài cực đại của chuỗi con có ký tự là: {chuoi_cuoi}")
