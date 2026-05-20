# --- Nhập danh sách cho đến khi gặp số 0 ---
lst = []
while True:
    num = int(input("Nhập số tự nhiên (nhập 0 để dừng): "))
    if num == 0:
        break
    lst.append(num)

print("Danh sách ban đầu:", lst)

#1
lst_insert = lst.copy()
lst_insert.append([1, 2, 3])
if len(lst_insert) >= 4:
    lst_insert.insert(4, [1, 2, 3])
else:
    print("Danh sách không đủ 5 phần tử để chèn vào vị trí thứ 5!")

lst_insert.insert(0, [1, 2, 3])
print("Sau khi chèn [1, 2, 3]:", lst_insert)

#2
k = int(input("Nhập vị trí k cần xóa (bắt đầu từ 1): "))
if 1 <= k <= len(lst):
    del lst[k - 1]
    print(f"Danh sách sau khi xóa phần tử thứ {k}:", lst)
else:
    print("Vị trí k không hợp lệ!")

#3
lst_tang = lst.copy()
lst_tang.sort()
print("Sắp xếp tăng dần:", lst_tang)

lst_giam = lst.copy()
lst_giam.sort(reverse=True)
print("Sắp xếp giảm dần:", lst_giam)