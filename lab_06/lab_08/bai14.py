def binh_phuong():
    n = int(input("Nhap n: "))
    ds = []
    for i in range(n):
        x = int(input("Nhap so: "))
        ds.append(x)
    kq = list(map(lambda x: x ** 2, ds))
    print(kq)
print("binh phuong: ")
