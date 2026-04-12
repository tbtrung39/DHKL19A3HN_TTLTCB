mat_khau = input("Nhap mat khau: ")
co_chu_thuong = False
co_chu_hoa = False
co_so = False
co_ky_tu_db = False
ky_tu_db = "$#@"
for ky_tu in mat_khau:
    if ky_tu >= 'a' and ky_tu <= 'z':
        co_chu_thuong = True
    if ky_tu >= 'A' and ky_tu <= 'Z':
        co_chu_hoa = True
    if ky_tu >= '0' and ky_tu <= '9':
        co_so = True
    if ky_tu in ky_tu_db:
        co_ky_tu_db = True
do_dai = len(mat_khau)
if (co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_db
    and do_dai >= 6 and do_dai <= 12):
    print("Mat khau hop le")
else:
    print("Mat khau khong hop le")