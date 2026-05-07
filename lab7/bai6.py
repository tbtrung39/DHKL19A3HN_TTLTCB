n = int(input("Nhap n: "))
day_so_nt = []
so = 2
while len(day_so_nt) < n:
    check = True
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            check = False
            break
    if check:
        day_so_nt.append(so)
    so = so + 1
print(day_so_nt)