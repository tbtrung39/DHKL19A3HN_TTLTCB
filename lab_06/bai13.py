chu_ngu = ["Anh", "Em"]
dong_tu = ["Chơi", "Đại"]
tan_ngu = ["Bóng đá", "Bóng rổ"]

cau_hoi = []

for i in range(len(chu_ngu)):
    for j in range(len(dong_tu)):
        for k in range(len(tan_ngu)):
            cau = chu_ngu[i] + " " + dong_tu[j] + " " + tan_ngu[k]
            cau_hoi.append(cau)

for i in range(len(cau_hoi)):
    print(cau_hoi[i])
