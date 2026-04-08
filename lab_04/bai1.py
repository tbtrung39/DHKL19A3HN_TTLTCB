while True:
    n = int(input("Nhập n nguyên dương: "))
    if n > 0: break
    print("Vui lòng nhập lại!")

# a) S4 = 1^2 + 2^2 + ... + n^2
s4 = 0
i = 1
while i <= n:
    s4 += i**2
    i += 1

# b) S5 = 1^3 + 3^3 + ... + (2n+1)^3
s5 = 0
i = 0
while i <= n:
    s5 += (2*i + 1)**3
    i += 1

# c) S6 = 2^4 + 4^4 + ... + (2n)^4
s6 = 0
i = 1
while i <= n:
    s6 += (2*i)**4
    i += 1

print(f"S4 = {s4}, S5 = {s5}, S6 = {s6}")