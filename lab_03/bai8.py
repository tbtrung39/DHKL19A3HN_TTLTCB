n = int(input("nhập vào số nguyên dương n: "))
if n <= 0: #lap3 chưa học while
    n = int(input("vui lòng nhập lại số nguyên n(>0): "))
print("a)")
S1 = 0
for i in range(1,n+1):
    S1 += i
print("Tổng S1 là: ",S1)
print("b)")
S2 = 0
for i in range(n+1):
    S2 += 2*i + 1 
print("Tổng S2 là: ",S2)
print("c)")
S3 = 0
for i in range(n+1):
    S3 += 2*i
print("Tổng S3 là: ",S3)