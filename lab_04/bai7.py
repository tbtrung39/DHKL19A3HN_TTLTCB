a = int(input("Số nguyên thứ nhất: "))
b = int(input("Số nguyên thứ hai: "))

a = abs(a)
b = abs(b)

# Nếu một trong hai số bằng 0 thì không có BCNN
if a == 0 or b == 0:
    print("Không có Bội chung nhỏ nhất khi có số 0.")
else:
    if a > b:
        so_lon_nhat = a
    else:
        so_lon_nhat = b
    
    bcnn = so_lon_nhat


    while True:
        if bcnn % a == 0 and bcnn % b == 0:
            print(f"Bội chung nhỏ nhất là: {bcnn}")
            break 
        bcnn += so_lon_nhat
  