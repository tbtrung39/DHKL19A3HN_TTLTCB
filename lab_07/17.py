n = int(input("Nhap so sinh vien: "))
du_lieu = {}

for i in range(n):
    while True:
        ma = input("Nhap ma SV (6 ky tu): ")
        if len(ma) == 6:
            break
    ten = input("Nhap ten SV: ")
    diem = round(float(input("Nhap diem (0-10): ")))
    du_lieu[ma] = [ten, diem]

danh_sach_sx = sorted(du_lieu.items(), key=lambda x: x[1][1], reverse=True)

for sv in danh_sach_sx:
    print(f"Ma: {sv[0]}, Ten: {sv[1][0]}, Diem: {sv[1][1]}")