n = 0
while n <= 0:
    n = int(input("Nhập n (n > 0): "))

s4 = sum(i**2 for i in range(1, n + 1))
s5 = sum(i**3 for i in range(1, 2*n + 2, 2)) 
s6 = sum(i**4 for i in range(2, 2*n + 1, 2)) 

print(f"S4 = {s4}, S5 = {s5}, S6 = {s6}")