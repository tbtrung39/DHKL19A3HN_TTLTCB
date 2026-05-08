n = int(input("Nhập độ dài của set A: "))
m = int(input("Nhập độ dài của set B: "))
A = set()
B = set()
for i in range(n):
    A.add(input(f"Nhập phần tử thứ {i + 1} của set A: "))
print("Set A:\n", A)
for ii in range(m):
    B.add(input(f"Nhập phần tử thứ {ii + 1} của set B: "))
print(f"Set B:\n {B}")
print(f"Phần tử giao A và B là: {A & B}")