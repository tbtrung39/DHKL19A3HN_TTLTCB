s = input("Nhap chuoi Hex: ")
hex_str = ""
for c in s:
    if ('0' <= c <= '9') or ('A' <= c <= 'F'):
        hex_str = hex_str + c
print("Chuoi Hex hop le:", hex_str)
tong = 0
mu = 0
for i in range(len(hex_str)-1, -1, -1):
    c = hex_str[i]
    if '0' <= c <= '9':
        value = ord(c) - ord('0')
    else:
        value = ord(c) - ord('A') + 10
    tong = tong + value * (16 ** mu)
    mu = mu + 1
print("So thap phan:", tong)