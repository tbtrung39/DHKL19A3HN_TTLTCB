def tim_min_max(a, b, c):
    min_val = a
    max_val = a
    
    if b < min_val:
        min_val = b
    if c < min_val:
        min_val = c
    
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    
    return min_val, max_val

a = int(input("Nhập số thứ 1: "))
b = int(input("Nhập số thứ 2: "))
c = int(input("Nhập số thứ 3: "))

min_val, max_val = tim_min_max(a, b, c)
print(f"Số nhỏ nhất: {min_val}")
print(f"Số lớn nhất: {max_val}")
