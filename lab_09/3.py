def luy_thua(a, n):
    if n == 0:
        return 1
    else:
        return a * luy_thua(a, n - 1)
a = int(input("Nhap a: "))
n = int(input("Nhap n: "))
x= luy_thua(a,n)
print("luy thua a^n =",x )