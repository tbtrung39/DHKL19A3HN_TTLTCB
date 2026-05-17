List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

print("Danh sách List_:")
for i in range(len(List_)):
    print(List_[i])

print("\nPhần tử thứ hai (index 1) của sublist thứ 3 (index 2):", List_[2][1])

import random
new_sublist = ["new_day", random.randint(50, 150)]
List_.append(new_sublist)
print("\nDanh sách sau khi thêm sublist ngẫu nhiên:")
for i in range(len(List_)):
    print(List_[i])

print("\nĐộ dài của danh sách:", len(List_))

ngay_can_tinh = []
for i in range(len(List_)):
    if List_[i][0] == "tue" or List_[i][0] == "wed" or List_[i][0] == "sat" or List_[i][0] == "sun":
        ngay_can_tinh.append(List_[i])

tong = 0
for i in range(len(ngay_can_tinh)):
    tong = tong + ngay_can_tinh[i][1]

print("Tổng sale value (thứ 2, thứ 3, thứ 7, chủ nhật):", tong)
