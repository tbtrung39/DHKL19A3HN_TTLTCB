n = int(input("Nhập bậc n của matrix đơn vị: "))
matrix = []
for i in range(n):
    mang_phu = [0]*n
    matrix.append(mang_phu)
    for j in range(n):
        if(i == j):
            matrix[i][j] = 1
for k in matrix:
    print(k)