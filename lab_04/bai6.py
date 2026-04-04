# Nhập số từ bàn phím
n = int(input("Nhập vào một số nguyên dương: "))

if n == 0:
    print("Không")
else:
    ket_qua = ""
    while n > 0:

        chu_so = n % 10

        if chu_so == 0:
            chu = "Không"
        elif chu_so == 1:
            chu = "Một"
        elif chu_so == 2:
            chu = "Hai"
        elif chu_so == 3:
            chu = "Ba"
        elif chu_so == 4:
            chu = "Bốn"
        elif chu_so == 5:
            chu = "Năm"
        elif chu_so == 6:
            chu = "Sáu"
        elif chu_so == 7:
            chu = "Bảy"
        elif chu_so == 8:
            chu = "Tám"
        elif chu_so == 9:
            chu = "Chín"
            
        ket_qua = chu + " " + ket_qua       
        n = n // 10
    print("Số bằng chữ là:", ket_qua)