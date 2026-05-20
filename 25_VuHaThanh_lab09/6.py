import random

n = int(input("Nhập số tự nhiên n: "))

#1
A = list(range(1, n + 1))
result = []

print(f"Dãy A ban đầu: {A}")
print("-" * 30)

while len(A) > 0:
    vi_tri_ngau_nhien = random.randint(0, len(A) - 1)
    phan_tu_lay_ra = A.pop(vi_tri_ngau_nhien)
    result.append(phan_tu_lay_ra)
    print(f"Lấy số {phan_tu_lay_ra} -> Dãy A còn lại: {A} -> Dãy result hiện tại: {result}")

print("-" * 30)
print(f"Hoán vị ngẫu nhiên cuối cùng (result): {result}")