import random
a = []
for i in range(1000):
    a.append(random.randint(1, 99999))
print("Danh sách 1000 số ngẫu nhiên (hiển thị 10 số đầu):", a[:10])
