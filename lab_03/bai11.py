n = int(input("Nhap  n: "))
while n<=0:
    n = int(input("Nhap lai "))
#a
for i in range(1, n+1):
    for j in range(i):
        print("*",end=" ")
    print()
#b
for i in range(1, n+1):
    for j in range(1, i+1):
        if j == 1 or j ==i or i ==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#c
for i in range(1,n +1):
    for j in range(n - i):
        print(" ", end = "")
    for j in range(2*i -1):
        print("*", end = " ")
    print()