n = int(input("Nhập số nguyên dương: "))
while n<=0:
    n = int(input("Nhập lại n > 0: "))

i = 2
while n > 1:
    if n % i==0:
        print(i)
        n = n // i
    else:
        i +=1
