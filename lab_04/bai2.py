n = int(input("Nhập số lượng số hạng n: "))

# a) S = 1/1 - 1/2 + 1/3 - 1/4...
sa = sum((-1)**(i) / (i+1) for i in range(n))

# b) S = 1/2 + 1/(2*3) + 1/(3*4)...
sb = sum(1 / (i * (i+1)) for i in range(2, n + 2))

# c) S = 1/sqrt(2) + 1/sqrt(3)...
import math
sc = sum(1 / math.sqrt(i) for i in range(2, n + 2))

print(f"Sa = {sa:.4f}, Sb = {sb:.4f}, Sc = {sc:.4f}")