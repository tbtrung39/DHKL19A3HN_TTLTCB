def la_so_nguyen_to(x):
    if x < 2: return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: return False
    return True

n = int(input("Nhập n: "))
if la_so_nguyen_to(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không là số nguyên tố.")
    # Tìm số gần nhất
    thap = n - 1
    cao = n + 1
    while True:
        if la_so_nguyen_to(thap) and thap > 1:
            print(f"Số nguyên tố gần nhất là: {thap}")
            break
        if la_so_nguyen_to(cao):
            print(f"Số nguyên tố gần nhất là: {cao}")
            break
        thap -= 1
        cao += 1