str = input("Nhap chuoi: ").upper()
hex_chars = "0123456789ABCDEF"
k = True
for ch in str:
    if ch not in hex_chars:
        k = False
if k:
    print("La chuoi Hex")
    print("So thap phan:", int(str, 16))
else:
    new_str = ""
    for ch in str:
        if ch in hex_chars:
            new_str += ch
    print("Chuoi sau khi loc:", new_str)
    if new_str != "":
        print("So thap phan:", int(new_str, 16))