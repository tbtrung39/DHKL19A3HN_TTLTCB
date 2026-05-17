def tim_bo_tham_so(n, index=1, tong=0, ket_qua=None):
    if ket_qua is None:
        ket_qua = []
    
    if tong == n:
        ket_qua.append([])
        return ket_qua
    
    if index > n:
        return ket_qua
    
    if tong + index <= n:
        tim_bo_tham_so(n, index + 1, tong + index, ket_qua)
    
    tim_bo_tham_so(n, index + 1, tong, ket_qua)
    
    return ket_qua

def tim_tap_con(n, index=1, danh_sach=None):
    if danh_sach is None:
        danh_sach = []
    
    ket_qua = []
    
    def de_qui(index, danh_sach_hien_tai):
        if index > n:
            if sum(danh_sach_hien_tai) == n:
                ket_qua.append(danh_sach_hien_tai[:])
            return
        
        de_qui(index + 1, danh_sach_hien_tai + [index])
        de_qui(index + 1, danh_sach_hien_tai)
    
    de_qui(1, [])
    return ket_qua

n = int(input("Nhập n: "))
ket_qua = tim_tap_con(n)

print(f"Các bộ số có tổng bằng {n} từ [1, 2, ..., {n}]:")
for bo in ket_qua:
    print(bo)
print(f"Tổng cộng {len(ket_qua)} bộ")
