s = input("Nhập chuỗi hệ Hex: ").upper()
chuoi_hex_hop_le = ""
ky_tu_hex = "0123456789ABCDEF"

for ky_tu in s:
    if ky_tu in ky_tu_hex:
        chuoi_hex_hop_le += ky_tu

if chuoi_hex_hop_le == "":
    print("Không có ký tự Hex hợp lệ nào.")
else:
    if chuoi_hex_hop_le != s:
        print("Chuỗi có ký tự không hợp lệ. Đã lọc còn lại:", chuoi_hex_hop_le)
    so_thap_phan = int(chuoi_hex_hop_le, 16)
    
    print("Giá trị thập phân tương ứng là:", so_thap_phan)