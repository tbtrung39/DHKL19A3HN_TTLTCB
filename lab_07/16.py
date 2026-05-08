A = [1, 2, 3, 2, 4]
n = len(A)
ket_qua = []

for i in range(n):
    for j in range(i + 1, n):
        if A[i] + 1 == A[j]:
            ket_qua.append((i, j))

print(ket_qua)