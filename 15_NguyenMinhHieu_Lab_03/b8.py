n = int(input("Nhập n: "))
if(n < 0):
    print("Nhập lại!")
else:
    s1 = 0
    s2 = 0
    s3 = 0
    for i in range(n+1):
        s1 += i
        s2 += 2*i + 1
        s3 += 2*i
    print(f"Giá trị của S1 là: {s1}")
    print(f"Giá trị của S2 là: {s2}")
    print(f"Giá trị của S3 là: {s3}")