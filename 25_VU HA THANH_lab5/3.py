try:
    n = int(input("Nhập một số tự nhiên n: "))
    
    if n < 0:
        print("Vui lòng nhập số tự nhiên (>= 0).")
    else:
        chuoi_bin = bin(n)
        ket_qua = chuoi_bin[2:]
        
        print(f"Số {n} trong hệ nhị phân là: {ket_qua}")

except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")