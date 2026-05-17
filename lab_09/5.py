def permutation(n):
    if n == 1:
        return [[1]]
    kq = []
    ds = permutation(n - 1)
    for p in ds:
        for i in range(len(p) + 1):
            moi = p[:i] + [n] + p[i:]
            kq.append(moi)
    return kq
n = int(input("Nhap n: "))
print(permutation(n))