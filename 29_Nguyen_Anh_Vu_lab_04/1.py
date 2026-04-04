n = int(input("Nhập n: "))
while n <=0:
    print("Nhập lại n > 0")
    
S4 = 0
i = 0
while i <= n:
    s4 +=  i**2
    i += 1
print(f"S4= {S4}")

S5 = 0
i = 0
while i <= 2 * n + 1:
        S5 += i ** 3
i += 1
print(f"S5 = {S5}")

S6 = 0
i = 2
while i <= 2 * n:
    S6 += i ** 4
    i += 2
print(f"S6 = {S6}")