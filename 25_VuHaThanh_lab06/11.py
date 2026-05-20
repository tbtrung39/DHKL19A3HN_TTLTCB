import random

n = int(input("Nhập số lượng phần tử n của danh sách A: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
print("-" * 30)
print("Danh sách A ban đầu:", A)
print("-" * 30)

#a
B = [i for i in A if i % 3 == 0 and i % 5 != 0]
print("Câu a - Danh sách B (chia hết cho 3, không chia hết cho 5):", B)

#b
C = [i**2 for i in A]
print("Câu b - Danh sách C (bình phương của A):", C)

#c
cac_so_chia_het_cho_3 = [i for i in A if i % 3 == 0]

số_luong_lay = random.randint(1, len(cac_so_chia_het_cho_3)) if cac_so_chia_het_cho_3 else 0

if số_luong_lay > 0:
    D = random.sample(cac_so_chia_het_cho_3, số_luong_lay)
else:
    D = [] 

print("Câu c - Danh sách D (các số chia hết cho 3 được bốc ngẫu nhiên):", D)