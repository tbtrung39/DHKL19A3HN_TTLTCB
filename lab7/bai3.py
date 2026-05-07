import random
n = int(input("Nhap n: "))
tap_hop_A = set()

while len(tap_hop_A) < n:
    tap_hop_A.add(random.random() * 100)

print(tap_hop_A)
print("Min:", min(tap_hop_A))
print("Max:", max(tap_hop_A))
print("Tong:", sum(tap_hop_A))