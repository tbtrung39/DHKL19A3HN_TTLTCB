a = [ 2, -4, 1, 9, -3, 6, 3, -2, 6, 8 ]

tong = sum(a)
print("Tổng:", tong)


duong = [x for x in a if x >= 0]
print("Số lượng dương:", len(duong), "- Tổng dương:", sum(duong))

for i, x in enumerate(a):
    if x < 0:
        print("Phần tử âm đầu tiên vị trí:", i, "- Giá trị:", x)
        break

for i, x in reversed(list(enumerate(a))):
    if x > 0:
        print("Phần tử dương cuối cùng vị trí:", i, "- Giá trị:", x)
        break

max_val = max(a)
for i, x in reversed(list(enumerate(a))):
    if x == max_val:
        print("Phần tử lớn nhất:", max_val, "- Vị trí cuối cùng:", i)
        break