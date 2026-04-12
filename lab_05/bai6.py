s = input("Nhập chuỗi Hex: ")
hex_digits = "0123456789ABCDEFabcdef"

filtered_hex = "".join([c for c in s if c in hex_digits])

if filtered_hex == s:
    print(f"Chuỗi '{s}' hợp lệ trong hệ Hex.")
else:
    print(f"Chuỗi không hợp lệ. Chuỗi sau khi lọc: {filtered_hex}")

if filtered_hex:
    decimal_val = int(filtered_hex, 16)
    print(f"Giá trị thập phân: {decimal_val}")