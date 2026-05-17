n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    x = int(input("Nhập phần tử thứ " + str(i+1) + ": "))
    a.append(x)

print("Danh sách:", a)

max1 = a[0]
max2 = -1
vi_tri_max2 = -1
for i in range(n):
    if a[i] > max1:
        max2 = max1
        max1 = a[i]
    elif a[i] > max2 and a[i] != max1:
        max2 = a[i]
        vi_tri_max2 = i
print("Phần tử lớn thứ hai:", max2, "- Vị trí:", vi_tri_max2)

max_count = 0
current_count = 0
for i in range(n):
    if a[i] > 0:
        current_count = current_count + 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0
print("Số dương liên tiếp nhiều nhất:", max_count)

max_sum = 0
current_sum = 0
for i in range(n):
    if a[i] > 0:
        current_sum = current_sum + a[i]
        if current_sum > max_sum:
            max_sum = current_sum
    else:
        current_sum = 0
print("Tổng số dương liên tiếp lớn nhất:", max_sum)
