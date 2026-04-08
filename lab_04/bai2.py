n = int(input("Nhập số lượng số hạng n: "))

# a) 
sa = sum((-1)**(i) / (i+1) for i in range(n))

# b) 
sb = sum(1 / (i * (i+1)) for i in range(2, n + 2))

# c) 
import math
sc = sum(1 / math.sqrt(i) for i in range(2, n + 2))

print(f"Sa = {sa:.4f}, Sb = {sb:.4f}, Sc = {sc:.4f}")