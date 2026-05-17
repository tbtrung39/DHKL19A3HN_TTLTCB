def rut_gon_phan_so(tu, mau):
    def ucln(a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
    
    uc = ucln(abs(tu), abs(mau))
    tu_rut = tu // uc
    mau_rut = mau // uc
    
    if mau_rut < 0:
        tu_rut = -tu_rut
        mau_rut = -mau_rut
    
    return tu_rut, mau_rut

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

tu_rut, mau_rut = rut_gon_phan_so(tu, mau)
print(f"Phân số rút gọn: {tu_rut}/{mau_rut}")
