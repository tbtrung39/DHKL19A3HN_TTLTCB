bin_str = input("Nhập chuỗi nhị phân (chỉ 0 và 1): ")
dec_val = 0
length = len(bin_str)

for i in range(length):
    bit = int(bin_str[i])
    dec_val += bit * (2 ** (length - 1 - i))
    
print("Số thập phân tương ứng:", dec_val)