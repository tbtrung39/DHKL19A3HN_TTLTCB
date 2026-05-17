def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Nhập n: "))

A = set()
for i in range(2, n + 1):
    if is_prime(i):
        A.add(i)

B = set()
for i in range(2, n + 1, 2):
    B.add(i)

print("Set A (các số nguyên tố không vượt quá n):", A)
print("Set B (các số chẵn không vượt quá n):", B)

common = A.intersection(B)
print("Phần tử chung:", common)

only_A = A.difference(B)
print("Phần tử chỉ thuộc A:", only_A)

only_B = B.difference(A)
print("Phần tử chỉ thuộc B:", only_B)

union = A.union(B)
print("Hợp của A và B:", union)
