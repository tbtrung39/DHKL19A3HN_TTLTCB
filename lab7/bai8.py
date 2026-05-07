A = {1, 2.5, "Hello", 10, 3.14, "Python", 7}
so_nguyen = 0
so_thuc = 0
chuoi = 0
for x in A:
    if type(x) == int:
        so_nguyen = so_nguyen + 1
    elif type(x) == float:
        so_thuc = so_thuc + 1
    elif type(x) == str:
        chuoi = chuoi + 1
print("Nguyen:", so_nguyen)
print("Thuc:", so_thuc)
print("Chuoi:", chuoi)