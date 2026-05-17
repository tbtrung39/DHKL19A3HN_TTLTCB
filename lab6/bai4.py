a = []
x = int(input("Nhập phần tử (nhập 0 để dừng): "))
while x != 0:
    a.append(x)
    x = int(input("Nhập phần tử (nhập 0 để dừng): "))

print("Danh sách ban đầu:", a)

a_dau = [1, 2, 3]
for i in range(len(a)):
    a_dau.append(a[i])
print("Chèn [1,2,3] vào đầu:", a_dau)

a_cuoi = []
for i in range(len(a)):
    a_cuoi.append(a[i])
a_cuoi.append(1)
a_cuoi.append(2)
a_cuoi.append(3)
print("Chèn [1,2,3] vào cuối:", a_cuoi)

a_vi_tri_5 = []
for i in range(len(a)):
    if i == 4:
        a_vi_tri_5.append(1)
        a_vi_tri_5.append(2)
        a_vi_tri_5.append(3)
    a_vi_tri_5.append(a[i])
if len(a) <= 4:
    a_vi_tri_5.append(1)
    a_vi_tri_5.append(2)
    a_vi_tri_5.append(3)
print("Chèn [1,2,3] vào vị trí thứ 5:", a_vi_tri_5)

k = int(input("Nhập vị trí k cần xóa (từ 1): "))
a_xoa = []
for i in range(len(a)):
    if i != k - 1:
        a_xoa.append(a[i])
print("Danh sách sau khi xóa vị trí", k, ":", a_xoa)

a_tang = []
for i in range(len(a)):
    a_tang.append(a[i])
for i in range(len(a_tang)):
    for j in range(i + 1, len(a_tang)):
        if a_tang[i] > a_tang[j]:
            temp = a_tang[i]
            a_tang[i] = a_tang[j]
            a_tang[j] = temp
print("Sắp xếp tăng dần:", a_tang)

a_giam = []
for i in range(len(a)):
    a_giam.append(a[i])
for i in range(len(a_giam)):
    for j in range(i + 1, len(a_giam)):
        if a_giam[i] < a_giam[j]:
            temp = a_giam[i]
            a_giam[i] = a_giam[j]
            a_giam[j] = temp
print("Sắp xếp giảm dần:", a_giam)
