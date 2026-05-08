n = int(input("Nhap so nhan vien: "))
ds_nv = {}

for i in range(n):
    ma = input("Nhap ma NV (4 ky tu): ")
    ten = input("Nhap ten (max 20 ky tu): ")[:20]
    nam_sinh = int(input("Nhap nam sinh: "))
    luong = int(input("Nhap luong: "))
    ds_nv[ma] = {"ten": ten, "nam_sinh": nam_sinh, "luong": luong}

x = input("Nhap ma NV can tim (x): ")
if x in ds_nv:
    print("Tim thay:", ds_nv[x])

y = input("Nhap ma NV tang luong (y): ")
if y in ds_nv:
    ds_nv[y]["luong"] += 1000000

z = input("Nhap ma NV can xoa (z): ")
if z in ds_nv:
    del ds_nv[z]

ds_giam_dan = sorted(ds_nv.items(), key=lambda x: x[1]["nam_sinh"], reverse=True)
print("Danh sach sau sap xep:", ds_giam_dan)