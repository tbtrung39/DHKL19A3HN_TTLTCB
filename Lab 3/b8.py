n = int(input("Nhap n: "))
while n <= 0:
    n = int(input("Nhap lai n > 0: "))

#a
S1 = 0
for i in range(1, n+1):
    S1 += i

#b
S2 = 0
for i in range(0, n+1):
    S2 += (2*i + 1)

#c
S3 = 0
for i in range(1, n+1):
    S3 += 2*i

print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)