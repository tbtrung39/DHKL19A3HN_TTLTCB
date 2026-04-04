n = int(input("Nhập độ rộng tam giác (n): "))
for i in range(n):
    chuoi = ""
    for j in range(2 * n - 1):
        if i == n - 1:
            if j % 2 == 0:
                chuoi = chuoi + "*"
            else:
                chuoi = chuoi + " "
        else:
            if j == n - 1 - i:
                chuoi = chuoi + "*"
            elif j == n - 1 + i:
                chuoi = chuoi + "*"
            else:
                chuoi = chuoi + " "
    print(chuoi)