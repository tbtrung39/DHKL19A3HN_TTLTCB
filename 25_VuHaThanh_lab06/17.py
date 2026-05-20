n = int(input("Nhập vào số nguyên n (bậc của ma trận): "))
ma_tran_don_vi = []
for i in range(n):
    hang_hien_tai = [] 
    for j in range(n):
        if i == j:
            hang_hien_tai.append(1)
        else:
            hang_hien_tai.append(0)
    ma_tran_don_vi.append(hang_hien_tai)

print(f"Ma trận đơn vị bậc {n} là:")
print(ma_tran_don_vi)
print("\nHiển thị dạng ma trận trực quan:")
for hang in ma_tran_don_vi:
    print(hang)