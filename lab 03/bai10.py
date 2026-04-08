n = int(input("Nhập số nguyên dương n: "))
print(f"{n} = ", end="")
i = 2
if n == 1:
    print(1)
while n > 1:
    if n % i == 0:
        print(i, end="")
        n //= i
        if n > 1:
            print(" x ", end="")
    else:
        i += 1