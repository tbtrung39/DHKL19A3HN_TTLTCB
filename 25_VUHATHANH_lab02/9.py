kw = float(input("Nhập số KW điện tiêu thụ: "))

if kw <= 100:
    tien_dien = kw * 2000
elif kw <= 200:
    tien_dien = kw * 2500
elif kw <= 300:
    tien_dien = kw * 3000
else:
    tien_dien = kw * 5000

print(f"Số tiền điện phải trả là: {tien_dien:,.0f} đồng")