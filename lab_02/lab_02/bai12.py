d = int(input("Ngay: "))
m = int(input("Thang: "))
y = int(input("Nam: "))
ngay = [31,28,31,30,31,30,31,31,30,31,30,31]
d += 1
if d > ngay[m-1]:
    d = 1
    m += 1
    if m > 12:
        m = 1
        y += 1
print("Ngay tiep theo:", d, m, y)