def tim_nghiem(n, tong, ds):
    if n == 1:
        print(ds + [tong])
        return
    for i in range(tong + 1):
        tim_nghiem(n - 1, tong - i, ds + [i])
N = int(input("Nhap N: "))
n = int(input("Nhap n: "))
print("Cac bo nghiem:")
tim_nghiem(n, N, [])