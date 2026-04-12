n = int(input("Nhập bậc của ma trận đơn vị n: "))
identity_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    identity_matrix.append(row)
print(f"Ma trận đơn vị bậc {n} là:")
for row in identity_matrix:
    print(row)