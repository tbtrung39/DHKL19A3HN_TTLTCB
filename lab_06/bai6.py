import random
A = [random.randint(1, 99999) for _ in range(1000)]
B = sorted(A)

for i in range(len(A)):
    for j in range(i+1, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]

print(B[:10])
print(A[:10])