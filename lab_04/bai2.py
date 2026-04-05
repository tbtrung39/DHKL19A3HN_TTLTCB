n = int(input("Nhập n:"))
Sa = 0
Sb = 0
Sc = 0
tong = 0
for i in range(1,n+1):
    if i % 2 == 1:
        S1 += 1 / i
    else:
        S1 -= 1 / i
for i in range(2, n + 2):
    tong += i
    S2 += 1 / tong
S3 = 0
for i in range(2, n + 2):
    S3 += 1 / (i**0.5)