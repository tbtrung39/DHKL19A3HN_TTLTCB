n = int(input("Nhap so: "))
if -100 < n < 100:
    print(0)
else:
    hang_tram = abs(n) // 100 % 10
    print(hang_tram)