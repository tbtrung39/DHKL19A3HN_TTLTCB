n = int(input("Nhập n: "))
print(f"Các số hoàn hảo nhỏ hơn {n}:")
for i in range(1, n):
    tong_uoc = 0
    for j in range(1, i):
        if i % j == 0:
            tong_uoc += j
    if tong_uoc == i:
        print(i, end=" ")