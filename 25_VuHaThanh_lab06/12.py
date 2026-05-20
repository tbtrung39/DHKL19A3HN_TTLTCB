so_du = 0

print("Nhập nhật ký giao dịch (Ví dụ: D 300 hoặc W 200). Nhấn Enter dòng trống để kết thúc:")
while True:
    dong_nhap = input()
    if not dong_nhap:
        break
    
    thong_tin = dong_nhap.split()
    hanh_dong = thong_tin[0]
    so_tien = int(thong_tin[1]) 
    if hanh_dong == "D" or hanh_dong == "d":
        so_du += so_tien  
    elif hanh_dong == "W" or hanh_dong == "w":
        so_du -= so_tien 
print("-" * 20)
print("Số tiền thực tế trong tài khoản là:", so_du)