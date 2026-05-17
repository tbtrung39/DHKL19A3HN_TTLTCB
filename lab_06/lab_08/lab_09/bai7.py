def nghiem(n, N, ds):
    if n == 1:
        print(ds + [N])
        return
    for i in range(N + 1):
        nghiem(n - 1, N - i, ds + [i])
n = int(input("Nhap n: "))
N = int(input("Nhap N: "))
nghiem(n, N, [])