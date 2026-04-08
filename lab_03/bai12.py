def tinh_check_digit(container_id):
    bang_ma = {
        'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
        'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
        'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
    }
    
    tong_trong_so = 0
    for n in range(10):
        ky_tu = container_id[n].upper()
        if ky_tu.isalpha():
            gia_tri = bang_ma[ky_tu]
        else:
            gia_tri = int(ky_tu)
        tong_trong_so += gia_tri * (2**n)
    check_digit = tong_trong_so % 11
    return check_digit % 10 
#Chạy thử với ví dụ trong đề: SUDU307007
ma_so = "SUDU307007"
ket_qua = tinh_check_digit(ma_so)
print(f"Mã số Container: {ma_so}")
print(f"Số kiểm tra (Check Digit) là: {ket_qua}")