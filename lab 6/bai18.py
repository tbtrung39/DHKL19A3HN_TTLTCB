# a. Viết chương trình nhập vào ma trận A
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

matrix_A = []
print(f"Nhập các phần tử của ma trận {m}x{n}:")
for i in range(m):
    row = []
    for j in range(n):
        val = int(input(f"Nhập phần tử A[{i}][{j}]: "))
        row.append(val)
    matrix_A.append(row)

# b. Tính tổng các phần tử của Ma trận A
total_sum = 0
for row in matrix_A:
    total_sum += sum(row)
print("Ma trận A vừa nhập:")
for row in matrix_A:
    print(row)
print(f"Tổng tất cả các phần tử trong ma trận A là: {total_sum}")