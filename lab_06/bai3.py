a = []
x = int(input("Nhập phần tử (nhập 0 để dừng): "))
while x != 0:
    a.append(x)
    x = int(input("Nhập phần tử (nhập 0 để dừng): "))

print("Danh sách ban đầu:", a)

duong = []
am_hoac_0 = []
for i in range(len(a)):
    if a[i] > 0:
        duong.append(a[i])
    else:
        am_hoac_0.append(a[i])
a = duong + am_hoac_0
print("Danh sách sau khi chuyển số dương lên đầu:", a)

m = int(input("Nhập số m cần chèn: "))
a_copy = []
for i in range(len(a)):
    a_copy.append(a[i])

a_dau = [m]
for i in range(len(a_copy)):
    a_dau.append(a_copy[i])
print("Chèn vào đầu danh sách:", a_dau)

a_cuoi = []
for i in range(len(a_copy)):
    a_cuoi.append(a_copy[i])
a_cuoi.append(m)
print("Chèn vào cuối danh sách:", a_cuoi)

a_vi_tri_5 = []
for i in range(len(a_copy)):
    if i == 4:
        a_vi_tri_5.append(m)
    a_vi_tri_5.append(a_copy[i])
if len(a_copy) <= 4:
    a_vi_tri_5.append(m)
print("Chèn vào vị trí thứ 5:", a_vi_tri_5)
