n = int(input("Nhap n: "))
A = set()
B = set()
for i in range(1, n + 1):
    if n % i == 0:
        check = True
        if i < 2:
            check = False
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                check = False
                break
        if check:
            A.add(i)

for i in range(2, n):
    if n % i != 0:
        check = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                check = False
                break
        if check:
            B.add(i)
print("A:", A)