n = int(input("Nhập vào 1 số nguyên: "))
for i in range(1,n): 
    tong = 0 
    for j in range(1,i):
        if i % j == 0:
            tong += j
    if tong == i:
        print("số hoàn hảo là: ",tong)
