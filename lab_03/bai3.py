n = int(input("nhập vào n: "))
snt = True
if n < 2:
    snt = False
else:
    for i in range(2,n):
        if n % i == 0:
            snt = False
            break
if snt:
    print(n," là số nguyên tố")
else:
    print(n," không là số nguyên tố")

for j in range(n-1,1,-1):
    la_snt = True
    for x in range(2,j):
        if j % x == 0:
            la_snt = False
            break
    if la_snt:
        print("số nguyên tố gần ",n," nhất là số",j)
        break