n = int(input("Nhap so nguyen duong n:"))
if n<=0:
    print("Nhap lai nha ban oi")
else:
#a
    s1 = 0
    for i in range(1, n+1):
       s1 +=i
       print("ket qua 1: ", s1)
#b
    s2 = 0
    for i in range(2, (2*n+1)+1, 2):
        s2 +=i
        print("ket qua 2: ", s2)
#c
    s3 =  0
    for i in range(2, (2*n)+1, 2):
        s3 +=i
        print("ket qua 3: ", s3)

