n = int(input("Nhap n: "))
A = []
for i in range(n):
    hang = []
    for j in range(n):
        if i == j:
            hang.append(1)
        else:
            hang.append(0)
    A.append(hang)
for i in A:
    print(i)