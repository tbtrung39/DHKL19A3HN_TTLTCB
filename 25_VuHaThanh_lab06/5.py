import random

A = [random.randint(1, 99999) for _ in range(1000)]
print("10 số đầu tiên trong danh sách là:", A[:10])
print("Tổng số phần tử trong list A là:", len(A))