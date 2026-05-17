import math

def tinh_chu_vi_hinh_tron(r):
    return 2 * math.pi * r

def tinh_dien_tich_hinh_tron(r):
    return math.pi * r * r

r = float(input("Nhập bán kính hình tròn: "))

chu_vi = tinh_chu_vi_hinh_tron(r)
dien_tich = tinh_dien_tich_hinh_tron(r)

print(f"Chu vi hình tròn: {chu_vi:.2f}")
print(f"Diện tích hình tròn: {dien_tich:.2f}")
