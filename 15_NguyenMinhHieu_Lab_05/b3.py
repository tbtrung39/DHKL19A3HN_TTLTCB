n = input("Nhập một chuỗi hệ cơ số 10(DEC): ")
n = int(n)
chuoi_bin = ""
while(n > 0 and n != 0):
    if(n % 2 == 0):
        n //= 2
        chuoi_bin = chuoi_bin + "0"
    else:
        n //= 2
        chuoi_bin = chuoi_bin + "1"
print(chuoi_bin[::-1])