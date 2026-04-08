n = int(input("Nhập n: "))
for i in range(2, n + 1):
    is_snt = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_snt = False
            break
    if is_snt:
        print(i, end=" ")