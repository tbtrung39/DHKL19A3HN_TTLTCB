s = input("Nhập chuỗi: ").upper()
hex_str = ""
for c in s:
    if ('0' <= c <= '9') or ('A' <= c <= 'F'):
        hex_str += c
print("Chuỗi Hex:", hex_str)
kq = 0
for c in hex_str:
    if '0' <= c <= '9':
        gt = ord(c) - ord('0')
    else:
        gt = ord(c) - ord('A') + 10
    kq = kq * 16 + gt

print("Số thập phân:", kq)