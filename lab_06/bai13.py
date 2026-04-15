chu_ngu = ["Anh","Em"]
dong_tu = ["Choi","Yeu"]
tan_ngu = ["Bong da","Bong ro"]

cau = [f"{a} {b} {c}" for a in chu_ngu for b in dong_tu for c in tan_ngu]

for x in cau:
    print(x)