
for a in range(100):
    n = int(input("nhap so nguyen duong n: "))
    if n > 0:
        break
    else:
        print("nhap lai")

#a
S1 = 0
for i in range(1,n+1):
    S1= S1 + i
print("S1 = ",S1)
#b
S2 = 0
for i in range(n + 1):
    S2 += 2 * i + 1
print("S2 = ",S2)
#c
S3 = 0
for i in range(1,n+1):
    S3 =S3 + 2*i
print("S3 = ",S3)

