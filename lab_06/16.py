so_hang = int(input("Nhập X (số hàng): "))
so_cot  = int(input("Nhập Y (số cột): "))

mang_hai_chieu = []
for i in range(so_hang):
    hang = []
    for j in range(so_cot):
        hang.append(i * j)
    mang_hai_chieu.append(hang)

print(mang_hai_chieu)