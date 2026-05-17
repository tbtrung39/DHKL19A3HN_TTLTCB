import random

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

A = set()
for i in range(5):
    x = random.choice(numbers)
    A.add(x)

print("Set A (5 phần tử ngẫu nhiên):", A)
