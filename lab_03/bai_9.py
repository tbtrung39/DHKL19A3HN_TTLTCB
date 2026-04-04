for a in range(100):
    n = int(input("Nhap so nguyen duong n: "))
    if n > 0:
        break
    else:
        print("nhap lai")
#a
s4 = 0
for i in range(1,n+1):
    s4 = s4 + i**2
print("s4 = ",s4)
#b
s5 = 0
for i in range(1,(2 * n + 1) + 1,2):
    s5 = s5 + i ** 3
print("s5 = ",s5)
#c
s6 = 0
for i in range(2,(2*n)+1,2):
    s6 = s6 + i**4
print("s6 = ",s6)
