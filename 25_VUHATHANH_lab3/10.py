n = int(input("Nhập số nguyên dương n: "))
print(f"{n} = ", end="")
d = 2
phân_tích = []

while n > 1:
    while n % d == 0:
        phân_tích.append(str(d))
        n //= d
    d += 1

print(" * ".join(phân_tích))
