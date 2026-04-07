n = int(input("Nhập chiều cao n: "))
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if j == n - i + 1 or j == n + i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 1. Thiết lập bảng tra cứu chữ cái
bang_tra = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
    'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
    'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}

ma_so = input("Nhập chuỗi container (10 ký tự, ví dụ SUDU307007): ").upper()

tong_trong_so = 0

for i in range(len(ma_so)):
    ky_tu = ma_so[i]
    
    if ky_tu.isalpha():
        gia_tri = bang_tra[ky_tu]
    else:
        gia_tri = int(ky_tu)
        
    trong_so = gia_tri * (2**i)
    tong_trong_so += trong_so
    print(f"w{i} = {gia_tri} * 2^{i} = {trong_so}")

so_kiem_tra = tong_trong_so % 11
print("-" * 20)
print(f"Tổng trọng số: {tong_trong_so}")
print(f"Số kiểm tra cuối cùng: {so_kiem_tra}")