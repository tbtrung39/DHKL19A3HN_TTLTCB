n =int(input("Nhập n :"))
while n <= 0 :
    print("n phải là 1 số nguyên dương!!!")
    n = int(input("Nhập lại số nguyên dương n :"))
for i in range(2,n+1):
    if n % i == 0:
        print(i,end = " ")
        n = n // i
    else :
        i += 1