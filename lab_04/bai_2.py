#a
n = int(input("Nhap n: "))
i = 1
s = 0
while i <= n:
    if i % 2 == 1:
        s = s + 1/i
    else:
        s = s - 1/i
    i = i + 1
print("S =", s)


#b
n = int(input("Nhap n: "))
i = 1
s = 0
while i <= n:
    s = s + 1/(i*(i+1))
    i = i + 1
print("S =", s)


#c
import math
n = int(input("Nhap n: "))
i = 2
s = 0
while i <= n:
    s = s + 1/math.sqrt(i)
    i = i + 1
print("S =", s)