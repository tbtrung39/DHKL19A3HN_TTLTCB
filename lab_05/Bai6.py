Str = input("Nhập chuỗi: ")
hex_chars = "0123456789ABCDEFabcdef"
is_hex = True

for c in Str:
    if c not in hex_chars:
        is_hex = False
        break

if is_hex:
    print("Chuỗi nhập vào hợp lệ trong hệ Hex.")
else:
    clean_str = ""
    for c in Str:
        if c in hex_chars:
            clean_str += c
            
    if clean_str != "":
        # Ép kiểu hệ 16 sang hệ thập phân
        dec_val = int(clean_str, 16) 
        print("Chuỗi sau khi loại bỏ ký tự không hợp lệ:", clean_str)
        print("Giá trị chuyển sang thập phân:", dec_val)
    else:
        print("Không còn ký tự Hex nào trong chuỗi.")