n = int(input("Nhập số nguyên n :"))
while n <= 0 :
    print("yêu nhập lại số nguyên dương n")
    n = int(input("Nhập lại n(n là số nguyên dương) :"))
s1 = s2 = s3 = 0
for i in range(1,n+1):
    s1 += i
    s2 += 2*i-1
    s3 += 2*i
print("s1 :",s1)
print("s2 :",s2)
print("s3 :",s3)