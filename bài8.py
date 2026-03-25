n = int(input("nhap n>0 : "))
while n <= 0:
    n = int(input("nhap lai n>0: "))

s1 = 0
for i in range(1, n+1):
    s1 += i
    print("s1=",s1)

s2 = 0
for i in range(0,n+1):
    s2 += (2*i+1)
    print("s2 =",s2)

s3 = 0
for i in range(1,n+1):
    s3 += 2*i
    print("s3 =",s3)