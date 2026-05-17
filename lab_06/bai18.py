m = int(input("Nhập m (số hàng): "))
n = int(input("Nhập n (số cột): "))

A = []
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input("Nhập A[" + str(i) + "][" + str(j) + "]: "))
        hang.append(x)
    A.append(hang)

print("Ma trận A:")
for i in range(len(A)):
    print(A[i])

tong = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        tong = tong + A[i][j]

print("Tổng các phần tử của ma trận A:", tong)
