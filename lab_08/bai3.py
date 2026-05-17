def la_so_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def tim_so_nguyen_to(n):
    danh_sach = []
    for i in range(2, n):
        if la_so_nguyen_to(i):
            danh_sach.append(i)
    return danh_sach

n = int(input("Nhập n: "))
so_nguyen_to = tim_so_nguyen_to(n)
print(f"Các số nguyên tố nhỏ hơn {n}:", so_nguyen_to)
