A_input = input("Nhập các phần tử của set A (cách nhau bằng dấu cách): ").split()
B_input = input("Nhập các phần tử của set B (cách nhau bằng dấu cách): ").split()

A = set(A_input)
B = set(B_input)

print("Set A:", A)
print("Set B:", B)

common = A.intersection(B)
print("Phần tử chung:", common)
