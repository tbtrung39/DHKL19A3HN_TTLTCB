Str = input("Nhập chuỗi: ")
tap_hex = "0123456789ABCDEFabcdef"
chuoi_hex_hop_le = ""
for c in Str:
    if c in tap_hex:
        chuoi_hex_hop_le += c
if len(chuoi_hex_hop_le) == len(Str):
    print("Chuỗi nhập vào là chuỗi Hex hợp lệ.")
else:
    print(f"Đã loại bỏ ký tự không hợp lệ. Chuỗi Hex còn lại: {chuoi_hex_hop_le}")
if chuoi_hex_hop_le:
    so_thap_phan = int(chuoi_hex_hop_le, 16)
    print(f"Số thập phân tương ứng: {so_thap_phan}")