so_hang = int(input("Nhập số hàng m: "))
so_cot  = int(input("Nhập số cột n: "))

ma_tran = []
for i in range(so_hang):
    hang = []
    for j in range(so_cot):
        gia_tri = int(input(f"Phần tử [{i}][{j}] = "))
        hang.append(gia_tri)
    ma_tran.append(hang)

print("Ma trận A:")
for hang in ma_tran:
    print(hang)

tong_phan_tu = 0
for i in range(so_hang):
    for j in range(so_cot):
        tong_phan_tu += ma_tran[i][j]

print("Tổng các phần tử:", tong_phan_tu)