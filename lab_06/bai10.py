import random

a = []
for i in range(0, 201):
    if i % 5 == 0 and i % 7 == 0:
        a.append(i)

print("Các số chia hết cho 5 và 7 từ 0 đến 200:", a)

if len(a) > 0:
    random_num = random.choice(a)
    print("Số ngẫu nhiên được chọn:", random_num)
