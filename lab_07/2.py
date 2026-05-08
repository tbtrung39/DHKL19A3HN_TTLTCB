import random as r
n = int(input("Nhập độ dài của Set: "))
numbers = set()
for i in range(1, n+1):
    numbers.add(int(input(f"Nhập phần tử thứ {i}: ")))
print("Set ban đầu là:", numbers)
k = r.randint(1, len(numbers))
A = set(r.sample(list(numbers), k))
print("Sinh tập hợp A:", A)