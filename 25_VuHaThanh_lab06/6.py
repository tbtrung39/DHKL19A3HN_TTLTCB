import random

A = [random.randint(1, 99999) for _ in range(1000)]

n = len(A)
for i in range(n - 1):
    vi_tri_min = i 
    
    for j in range(i + 1, n):
        if A[j] < A[vi_tri_min]:
            vi_tri_min = j
            
    A[i], A[vi_tri_min] = A[vi_tri_min], A[i]

print("Cách 2 (Tự viết thuật toán) - 10 số đầu tiên:")
print(A[:10])