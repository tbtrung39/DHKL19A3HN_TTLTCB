n = int(input("nhập vào số nguyên dương n: "))
if n <= 0: #lap3 chưa học while
    n = int(input("vui lòng nhập lại số nguyên n(>0): "))
print("a)")
S4 = 0
for i in range(1,n+1):
    S4 += i**2
print("Tổng S4 là: ",S4)
print("b)")
S5 = 0
for i in range(n+1):
    S5 += (2*i + 1 )**3
print("Tổng S5 là: ",S5)
print("c)")
S6 = 0
for i in range(n+1):
    S6 += (2*i)**4
print("Tổng S6 là: ",S6)