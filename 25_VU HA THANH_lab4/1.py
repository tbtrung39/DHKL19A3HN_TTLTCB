# Nhập n và kiểm tra điều kiện
n = 0
while n <= 0:
    n = int(input("Nhập n nguyên dương: "))

# a) S4 = 1^2 + 2^2 + ... + n^2
s4 = 0
i = 1
while i <= n:
    s4 += i**2
    i += 1
print("S4 =", s4)

# c) S6 = 2^4 + 4^4 + ... + (2n)^4
s6 = 0
i = 1
while i <= n:
    s6 += (2*i)**4
    i += 1
print("S6 =", s6)