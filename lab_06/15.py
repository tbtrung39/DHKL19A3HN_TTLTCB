so_luong = int(input("Nhập số lượng tuple: "))
danh_sach = []

for i in range(so_luong):
    dong = input("Nhập tên,tuổi,điểm: ").split(",")
    danh_sach.append((dong[0].strip(), int(dong[1].strip()), float(dong[2].strip())))

for i in range(len(danh_sach) - 1):
    for j in range(len(danh_sach) - i - 1):
        phan_tu_truoc = danh_sach[j]
        phan_tu_sau   = danh_sach[j + 1]
        can_doi = False

        if phan_tu_truoc[0] > phan_tu_sau[0]:
            can_doi = True
        elif phan_tu_truoc[0] == phan_tu_sau[0]:
            if phan_tu_truoc[1] > phan_tu_sau[1]:
                can_doi = True
            elif phan_tu_truoc[1] == phan_tu_sau[1]:
                if phan_tu_truoc[2] > phan_tu_sau[2]:
                    can_doi = True

        if can_doi:
            danh_sach[j], danh_sach[j + 1] = danh_sach[j + 1], danh_sach[j]

for phan_tu in danh_sach:
    print(phan_tu)