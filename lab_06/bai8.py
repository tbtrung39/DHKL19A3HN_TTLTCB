n = int(input("Nhap n: "))
a, b = 0, 1
fibonaic = []
for i in range(n):
    fibonaic.append(str(a))
    a, b = b, a + b
print(",".join(fibonaic))