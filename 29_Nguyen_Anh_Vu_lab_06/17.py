bac_n = int(input("Nhập n: "))

ma_tran_don_vi = []
for i in range(bac_n):
    hang = []
    for j in range(bac_n):
        if i == j:
            hang.append(1)
        else:
            hang.append(0)
    ma_tran_don_vi.append(hang)

for hang in ma_tran_don_vi:
    print(hang)