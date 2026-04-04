'''8. Viết chương trình tính lương của nhân viên dựa theo thâm niên công tác (TNCT) như sau:
Lương = hệ số × lương căn bản, trong đó lương căn bản là 1.350.000 đồng.
- Nếu TNCT < 12 tháng: hệ số = 2.34
- Nếu 12 ≤ TNCT < 36 tháng: hệ số = 3.33
- Nếu 36 ≤ TNCT < 60 tháng: hệ số = 3.66
- Nếu TNCT ≥ 60 tháng: hệ số = 3.99'''

tnct = int(input("Nhập thâm niên công tác: "))

luong_cb = 1350000

if tnct < 12:
    heso = 2.34
elif 12 <= tnct <= 36:
    heso = 3.33
elif 36 <= tnct <= 60:
    heso = 3.66
else:
    heso = 3.99
    
luong = heso * luong_cb

print("Số lương nhân viên nhận được: ", luong)