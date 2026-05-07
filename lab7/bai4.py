du_lieu = "161 182 161 154 176 170 167 171 170 174 150 142 148 165 170 178 156 145 149 163 162 159 165 165 170 180 155 159 155 153 152 162 180 168 169 168 167 170"
danh_sach_chieu_cao = du_lieu.split()

# a. Hoi nhom co bao nhieu sinh vien?
so_luong = len(danh_sach_chieu_cao)
print("So sinh vien:", so_luong)

# b. Tinh chieu cao trung binh
tong_chieu_cao = 0
for x in danh_sach_chieu_cao:
    tong_chieu_cao = tong_chieu_cao + int(x)

trung_binh = tong_chieu_cao / so_luong
print("Chieu cao trung binh:", trung_binh)