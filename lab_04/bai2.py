import math

#a
n = int(input("Nhap n: "))
S = 0
for i in range(2, n+2):
    S += 1/i
print("S =", S)

#b
n = int(input("Nhap n: "))
S = 0
for i in range(2, n+2):
    S += 1/(i*(i+1))
print("S=", S)

#c
n = int(input("Nhap n: "))
S = 0
for i in range(2, n+2):
    S += 1/math.sqrt(i)
print("S =", S)