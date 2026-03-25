n = int(input("nhap so nguyen duong: "))
print(f"{n} =",end="")
for i in range(2,n+1):
    while n % i == 0:
        print(i,end="")
        n = n// i
        if n >1:
            print("*",end="")