n = int(input("Nhập số nguyên có 3 chữ số: "))

if 100 <= n <= 999:
    tram = n // 100
    chuc = (n % 100) // 10
    donvi = n % 10
    
    chuoi = ""
    
    if tram == 1:
        chuoi = chuoi + "một trăm"
    elif tram == 2:
        chuoi = chuoi + "hai trăm"
    elif tram == 3:
        chuoi = chuoi + "ba trăm"
    elif tram == 4:
        chuoi = chuoi + "bốn trăm"
    elif tram == 5:
        chuoi = chuoi + "năm trăm"
    elif tram == 6:
        chuoi = chuoi + "sáu trăm"
    elif tram == 7:
        chuoi = chuoi + "bảy trăm"
    elif tram == 8:
        chuoi = chuoi + "tám trăm"
    elif tram == 9:
        chuoi = chuoi + "chín trăm"
        
    if chuc == 0:
        if donvi == 1:
            chuoi = chuoi + " lẻ một"
        elif donvi == 2:
            chuoi = chuoi + " lẻ hai"
        elif donvi == 3:
            chuoi = chuoi + " lẻ ba"
        elif donvi == 4:
            chuoi = chuoi + " lẻ bốn"
        elif donvi == 5:
            chuoi = chuoi + " lẻ năm"
        elif donvi == 6:
            chuoi = chuoi + " lẻ sáu"
        elif donvi == 7:
            chuoi = chuoi + " lẻ bảy"
        elif donvi == 8:
            chuoi = chuoi + " lẻ tám"
        elif donvi == 9:
            chuoi = chuoi + " lẻ chín"
    elif chuc == 1:
        chuoi = chuoi + " mười"
        if donvi == 1:
            chuoi = chuoi + " một"
        elif donvi == 2:
            chuoi = chuoi + " hai"
        elif donvi == 3:
            chuoi = chuoi + " ba"
        elif donvi == 4:
            chuoi = chuoi + " bốn"
        elif donvi == 5:
            chuoi = chuoi + " lăm"
        elif donvi == 6:
            chuoi = chuoi + " sáu"
        elif donvi == 7:
            chuoi = chuoi + " bảy"
        elif donvi == 8:
            chuoi = chuoi + " tám"
        elif donvi == 9:
            chuoi = chuoi + " chín"
    else:
        if chuc == 2:
            chuoi = chuoi + " hai mươi"
        elif chuc == 3:
            chuoi = chuoi + " ba mươi"
        elif chuc == 4:
            chuoi = chuoi + " bốn mươi"
        elif chuc == 5:
            chuoi = chuoi + " năm mươi"
        elif chuc == 6:
            chuoi = chuoi + " sáu mươi"
        elif chuc == 7:
            chuoi = chuoi + " bảy mươi"
        elif chuc == 8:
            chuoi = chuoi + " tám mươi"
        elif chuc == 9:
            chuoi = chuoi + " chín mươi"
            
        if donvi == 1:
            chuoi = chuoi + " mốt"
        elif donvi == 2:
            chuoi = chuoi + " hai"
        elif donvi == 3:
            chuoi = chuoi + " ba"
        elif donvi == 4:
            chuoi = chuoi + " tư"
        elif donvi == 5:
            chuoi = chuoi + " lăm"
        elif donvi == 6:
            chuoi = chuoi + " sáu"
        elif donvi == 7:
            chuoi = chuoi + " bảy"
        elif donvi == 8:
            chuoi = chuoi + " tám"
        elif donvi == 9:
            chuoi = chuoi + " chín"
            
    print("Cách đọc là:", chuoi)
else:
    print("Số nhập vào không hợp lệ (phải là số có 3 chữ số)")