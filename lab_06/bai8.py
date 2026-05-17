n = int(input("Nhập n: "))

fib = []
for i in range(n):
    if i == 0:
        fib.append(0)
    elif i == 1:
        fib.append(1)
    else:
        fib.append(fib[i-1] + fib[i-2])

result = ""
for i in range(len(fib)):
    if i == 0:
        result = str(fib[i])
    else:
        result = result + ", " + str(fib[i])

print("Dãy Fibonacci:", result)
