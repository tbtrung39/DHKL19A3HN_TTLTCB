import random

n = int(input("n = "))

A = list(range(1, n + 1))
result = []

while len(A) > 0:
    vitri = random.randint(0, len(A) - 1)
    result.append(A[vitri])
    A.pop(vitri)

print("Hoán vị ngẫu nhiên:", result)