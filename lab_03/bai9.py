while True:
    n = int(input("Nhập n nguyên dương: "))
    if n > 0: break
    print("Nhập lại!")
s4 = 0
for i in range(1, n + 1): s4 += i**2
s5 = 0
for i in range(n + 1): s5 += (2*i + 1)**3
s6 = 0
for i in range(1, n + 1): s6 += (2*i)**4
print(f"S4 = {s4}, S5 = {s5}, S6 = {s6}")