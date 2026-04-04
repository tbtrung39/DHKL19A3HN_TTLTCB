n = int(input("Nhập n: "))
while n<=0:
    n = int(input("Nhập lại n > 0: "))

print("Câu a: \n")
for i in range(1, n+1):
    for j in range(i):
        print("*",end=" ")
    print()

print("Câu b: \n")    
for i in range(1, n+1):
    for j in range(1, i+1):
        if j == 1 or j ==i or i ==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("Câu c: \n")   
for i in range(1,n +1):
    for j in range(n - i):
        print(" ", end = "")
    for j in range(2*i -1):
        print("*", end = " ")
    print()