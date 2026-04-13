n = int(input("Nhập độ dài của matrix A: "))
m = int(input("Nhập độ dài của mảng phụ: "))
matrix_A = []
for i in range(n):
    mang_phu = []
    for j in range(m):
        mang_phu.append(int(input(f"Nhập phần tử hàng {i + 1}, cột {j + 1}: ")))
    matrix_A.append(mang_phu)
print("Matrix nhận được là:", matrix_A)
tong = 0
for tl in range(len(matrix_A)):
    tong += sum(matrix_A[tl])
print(tong)