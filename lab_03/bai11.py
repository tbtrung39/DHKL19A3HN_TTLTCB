print("a)")
h = int(input("Nhập giá trị chiều cao của tam giác :"))
for dong in range(1,h+1):
    for cot   in range(1,2*h):
        if cot == h - dong + 1 or cot == h + dong -1 or dong == h:
            print("*",end = " ")
        else :
            print(" ",end= " ")
    print( )

print("b)")
h = int(input("Nhập chiều cao của tam giác :"))
for i in range(1,h+1):
    for j in range(1,2*h):
        if(j == h-i+1 or j == h +i-1 or i == h) and i % 2 ==1:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print("\r")
print("c)")
h = int(input("Nhập chiều cao của tam giác :"))
k = 2*h -2
for dong in range(1,h+1):
    for cot in range(1,k+1):
        print(end=" ")
    for cot in range(1,dong +1):
        print("*",end= " ")
    k = k -1
    print("\r")