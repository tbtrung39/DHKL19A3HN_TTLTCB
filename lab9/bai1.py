def tim_max_3_so(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = int(input("Nhập số thứ 1: "))
b = int(input("Nhập số thứ 2: "))
c = int(input("Nhập số thứ 3: "))

max_val = tim_max_3_so(a, b, c)
print(f"Số lớn nhất trong {a}, {b}, {c} là: {max_val}")
