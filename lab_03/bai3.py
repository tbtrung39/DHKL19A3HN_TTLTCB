def check_snt(k):
    if k < 2: return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0: return False
    return True
n = int(input("Nhập n: "))
if check_snt(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")
    i = 1
    while True:
        if check_snt(n - i) and (n - i) > 1:
            print(f"Số nguyên tố gần nhất là: {n - i}")
            break
        if check_snt(n + i):
            print(f"Số nguyên tố gần nhất là: {n + i}")
            break
        i += 1