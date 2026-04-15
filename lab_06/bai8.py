n = int(input("Nhap n: "))
fib = [0, 1]
for i in range(2, n+2):
    fib.append(fib[i-1] + fib[i-2])
print("Day Fibonacci:")
print(", ".join(str(x) for x in fib))