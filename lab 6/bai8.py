n = int(input("Nhập n: "))
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(n-2)]
result = fib[:n]
print(", ".join(map(str, result)))