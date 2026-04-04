chuoi_1 = input("Nhập chuỗi Str1: ")
chuoi_2 = input("Nhập chuỗi Str2: ")
ket_qua = ""
do_dai_1 = len(chuoi_1)
do_dai_2 = len(chuoi_2)
do_dai_ngan = do_dai_1
if do_dai_2 < do_dai_1:
    do_dai_ngan = do_dai_2
for vi_tri in range(do_dai_ngan):
    ket_qua += chuoi_1[vi_tri] + chuoi_2[vi_tri]
if do_dai_1 > do_dai_2:
    for vi_tri in range(do_dai_ngan, do_dai_1):
        ket_qua += chuoi_1[vi_tri]
else:
    for vi_tri in range(do_dai_ngan, do_dai_2):
        ket_qua += chuoi_2[vi_tri]
print("Chuỗi sau khi trộn:", ket_qua)