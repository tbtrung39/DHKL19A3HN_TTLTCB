def tim_hoan_vi(danh_sach):
    if len(danh_sach) <= 1:
        return [danh_sach]
    
    ket_qua = []
    
    for i in range(len(danh_sach)):
        phan_tu_dau = danh_sach[i]
        phan_con_lai = danh_sach[:i] + danh_sach[i+1:]
        for hoan_vi_con in tim_hoan_vi(phan_con_lai):
            ket_qua.append([phan_tu_dau] + hoan_vi_con)
            
    return ket_qua

n = int(input("Nhập số tự nhiên n: "))
day_so = list(range(1, n + 1))
cac_hoan_vi = tim_hoan_vi(day_so)
print(f"Tất cả các hoán vị của dãy là:")
for hoan_vi in cac_hoan_vi:
    print(hoan_vi)
    
print(f"==> Tổng cộng có {len(cac_hoan_vi)} hoán vị.")
