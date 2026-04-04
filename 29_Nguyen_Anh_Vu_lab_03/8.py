n = int(input("Nhập số nguyên dương: "))
while n <= 0:
    n = int(input("Nhập lại n > 0: "))
    
s1 = 0
for i in range(1,n+1):
    s1 += i
print("S1 =",s1)
s2 =0
for i in range(1, n +1):
    s2 += 2*i - 1
print("S2 =",s2)
s3=0
for i in range(1, n +1):
    s3 += 2*i
print("S3 =", s3)