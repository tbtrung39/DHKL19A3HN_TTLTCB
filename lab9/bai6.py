import random

def hoan_vi_ngau_nhien(n):
    A = list(range(1, n + 1))
    result = []
    
    for i in range(n):
        index = random.randint(0, len(A) - 1)
        result.append(A[index])
        A.pop(index)
    
    return result

n = int(input("Nhập n: "))
hoan_vi = hoan_vi_ngau_nhien(n)

print(f"Hoán vị ngẫu nhiên của [1, 2, ..., {n}]: {hoan_vi}")
