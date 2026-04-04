n = int(input("Nhập vào n: "))
if n < 2:
    print(n,"không phải là số nguyên tố!")
for i in range(2,n+1):
    snt = True
    for j in range(2,i):
        if i % j == 0:
            snt = False
            break
    if snt:
        print("số nguyên tố là: ",i)