danh_sach_so = [2, 4, 6, 8, 10]
for so in danh_sach_so:
    assert so % 2 == 0, f"Phát hiện số lẻ: {so}! Tất cả phải là số chẵn."
print("Tuyệt vời! Tất cả các số trong danh sách đều là số chẵn.")