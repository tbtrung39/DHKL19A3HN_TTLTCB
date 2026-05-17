chu_ngu = ["Anh", "Em"]
dong_tu = ["Choi", "Yeu"]
tan_ngu = ["Bong da", "Bong ro"]
cau = [x + " " + y + " " + z
       for x in chu_ngu
       for y in dong_tu
       for z in tan_ngu]
for i in cau:
    print(i)