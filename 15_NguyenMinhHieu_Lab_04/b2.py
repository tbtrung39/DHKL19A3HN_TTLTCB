n = int(input("Nhập giá trị cuối: "))
s1 = 0
s2 = 0
s3 = 0
i = 1
dau = 1
while(i <= n):
    s1 += 1/(i*dau)
    print(s1)
    dau *= -1
    s2 += 1/(i*(i+1))
    s3 += 1/(i+1)**0.5
    i += 1
print(f"S1 = {s1}")
print(f"S2 = {s2}")
print(f"S3 = {s3}")