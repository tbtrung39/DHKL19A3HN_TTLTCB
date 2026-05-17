def permutation(n):
    if n == 1:
        return [[1]]
    else:
        ket_qua = []
        per_n_1 = permutation(n - 1)
        for perm in per_n_1:
            for i in range(len(perm) + 1):
                ket_qua.append(perm[:i] + [n] + perm[i:])
        return ket_qua

n = int(input("Nhập n: "))
ket_qua = permutation(n)

print(f"Tất cả các hoán vị của [1, 2, ..., {n}]:")
for perm in ket_qua:
    print(perm)
print(f"Tổng cộng {len(ket_qua)} hoán vị")
