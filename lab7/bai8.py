A = {1, 2.5, "hello", 3, 4.7, "world", 5, 6.2}

so_nguyen = 0
so_thuc = 0
chuoi = 0

for element in A:
    if isinstance(element, int):
        so_nguyen = so_nguyen + 1
    elif isinstance(element, float):
        so_thuc = so_thuc + 1
    elif isinstance(element, str):
        chuoi = chuoi + 1

print("Set A:", A)
print("Số phần tử là số nguyên:", so_nguyen)
print("Số phần tử là số thực:", so_thuc)
print("Số phần tử là chuỗi ký tự:", chuoi)
