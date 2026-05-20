def permutation(n):
    if n == 1:
        return [[1]]
    cac_hoan_vi_truoc = permutation(n - 1)
    ket_qua = []
    for hoan_vi in cac_hoan_vi_truoc:
        for i in range(len(hoan_vi) + 1):
            hoan_vi_moi = hoan_vi[:i] + [n] + hoan_vi[i:]
            ket_qua.append(hoan_vi_moi)
            
    return ket_qua

n = int(input("Nhập số nguyên n: "))

if n < 1:
    print("Vui lòng nhập số n >= 1!")
else:
    danh_sach_hoan_vi = permutation(n)
    
    print(f"Kết quả trả về của permutation({n}):")
    print(danh_sach_hoan_vi)