n= int(input("Nhập số tự nhiên n: "))
prime = set()
i = 2
while(len(prime) < n):
    kt = 1
    j = 2
    while j * j <= i: 
        if i % j == 0:
            kt = 0
            break
        j += 1
    if kt == 1:
        prime.add(i)
    i += 1
print(prime)