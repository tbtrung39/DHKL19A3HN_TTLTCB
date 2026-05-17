import random

a = []
for i in range(1000):
    a.append(random.randint(1, 99999))
print("Danh sách 1000 số ngẫu nhiên (hiển thị 5 số đầu):", a[:5])

a_tang_sorted = sorted(a)
print("Sắp xếp tăng dần (cách 1 - dùng sorted()):")
print("5 số đầu:", a_tang_sorted[:5])
print("5 số cuối:", a_tang_sorted[-5:])

a_tang_bubble = []
for i in range(len(a)):
    a_tang_bubble.append(a[i])

for i in range(len(a_tang_bubble)):
    for j in range(i + 1, len(a_tang_bubble)):
        if a_tang_bubble[i] > a_tang_bubble[j]:
            temp = a_tang_bubble[i]
            a_tang_bubble[i] = a_tang_bubble[j]
            a_tang_bubble[j] = temp

print("\nSắp xếp tăng dần (cách 2 - không dùng sorted()):")
print("5 số đầu:", a_tang_bubble[:5])
print("5 số cuối:", a_tang_bubble[-5:])
