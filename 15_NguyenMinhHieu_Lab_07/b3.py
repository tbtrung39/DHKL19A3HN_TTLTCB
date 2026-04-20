import random as rd
n = int(input("Nhập độ dài của set A: "))
A = set()
for i in range(n):
    A.add(rd.uniform(0, 100))
print("Set A:", A)
print("Phần tử nhỏ nhất:", min(A))
print("Phần tử lớn nhất:", max(A))
print("Tổng phần tử:", sum(A))