import random
def random_permutation(n):
    A = list(range(1, n + 1))
    result = []
    while len(A) > 0:
        x = random.choice(A)
        result.append(x)
        A.remove(x)
    return result
n = int(input("Nhập n: "))
print("Hoán vị ngẫu nhiên:", random_permutation(n))