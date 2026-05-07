mat_khau = input("Nhap mat khau: ")
hop_le = True

if len(mat_khau) < 6 or len(mat_khau) > 12:
    hop_le = False

co_chu_thuong = False
co_chu_hoa = False
co_so = False
co_ky_tu_dac_biet = False

for chu in mat_khau:
    if 'a' <= chu <= 'z':
        co_chu_thuong = True
    elif 'A' <= chu <= 'Z':
        co_chu_hoa = True
    elif '0' <= chu <= '9':
        co_so = True
    elif chu in "$#@":
        co_ky_tu_dac_biet = True

if not (co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_dac_biet):
    hop_le = False

if hop_le:
    print("Hop le")
else:
    print("Khong hop le")