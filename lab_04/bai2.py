n = int(input("Nhập n :"))
s1 = s2 = s3 = 0
i = 1
while i <=n:
    s1 +=((-1)**(i+1))/i
    s2 += 1/(i*(i+1))
    s3 += 1/((i+1)**0.5)
    i += 1
print("S1 =",s1)
print("S2 =",s2)
print("S3 =",s3)