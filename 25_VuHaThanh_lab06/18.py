# CÂU A: NHẬP MA TRẬN A KÍCH THƯỚC M x N TỪ BÀN PHÍM
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
A = []

print("\n--- Nhập các phần tử cho ma trận A ---")
for i in range(m):
    hang_hien_tai = []
    for j in range(n):
        gia_tri = int(input(f"Nhập phần tử A[{i}][{j}]: "))
        hang_hien_tai.append(gia_tri) 
        
    A.append(hang_hien_tai)
print("\nMa trận A vừa nhập là:")
for hang in A:
    print(hang)

# CÂU B: TÍNH TỔNG CÁC PHẦN TỬ CỦA MA TRẬN A
tong_ma_tran = 0
for hang in A:
    for phan_tu in hang:
        tong_ma_tran += phan_tu
print("-------------------------------------------------")
print(f"Tổng tất cả các phần tử của Ma trận A là: {tong_ma_tran}")