chuoi = input("Nhập mã container (10 ký tự, ví dụ SUDU307007): ")
tong = 0
chi_so = 0
for c in chuoi:
    gia_tri = 0
    if c == 'A':
        gia_tri = 10
    elif c == 'B':
        gia_tri = 12
    elif c == 'C':
        gia_tri = 13
    elif c == 'D':
        gia_tri = 14
    elif c == 'E':
        gia_tri = 15
    elif c == 'F':
        gia_tri = 16
    elif c == 'G':
        gia_tri = 17
    elif c == 'H':
        gia_tri = 18
    elif c == 'I':
        gia_tri = 19
    elif c == 'J':
        gia_tri = 20
    elif c == 'K':
        gia_tri = 21
    elif c == 'L':
        gia_tri = 23
    elif c == 'M':
        gia_tri = 24
    elif c == 'N':
        gia_tri = 25
    elif c == 'O':
        gia_tri = 26
    elif c == 'P':
        gia_tri = 27
    elif c == 'Q':
        gia_tri = 28
    elif c == 'R':
        gia_tri = 29
    elif c == 'S':
        gia_tri = 30
    elif c == 'T':
        gia_tri = 31
    elif c == 'U':
        gia_tri = 32
    elif c == 'V':
        gia_tri = 34
    elif c == 'W':
        gia_tri = 35
    elif c == 'X':
        gia_tri = 36
    elif c == 'Y':
        gia_tri = 37
    elif c == 'Z':
        gia_tri = 38
    elif c == '0':
        gia_tri = 0
    elif c == '1':
        gia_tri = 1
    elif c == '2':
        gia_tri = 2
    elif c == '3':
        gia_tri = 3
    elif c == '4':
        gia_tri = 4
    elif c == '5':
        gia_tri = 5
    elif c == '6':
        gia_tri = 6
    elif c == '7':
        gia_tri = 7
    elif c == '8':
        gia_tri = 8
    elif c == '9':
        gia_tri = 9
        
    luy_thua = 1
    for i in range(chi_so):
        luy_thua = luy_thua * 2
        
    tong = tong + gia_tri * luy_thua
    chi_so = chi_so + 1

so_kiem_tra = tong % 11
print("Tổng các trọng số là:", tong)
print("Số kiểm tra của mã container là:", so_kiem_tra)