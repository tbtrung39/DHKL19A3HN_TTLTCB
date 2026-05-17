X = int(input("Nhập X (số hàng): "))
Y = int(input("Nhập Y (số cột): "))

matrix = []
for i in range(X):
    hang = []
    for j in range(Y):
        hang.append(i * j)
    matrix.append(hang)

print("Ma trận:")
for i in range(len(matrix)):
    print(matrix[i])
