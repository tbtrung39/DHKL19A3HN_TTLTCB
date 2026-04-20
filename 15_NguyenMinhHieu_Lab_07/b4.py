ds_thong_ke = {
    161 : 2,
    182 : 1,
    154 : 1,
    176 : 1,
    170 : 5,
    167 : 2,
    171 : 1,
    174 : 1,
    150 : 1,
    142 : 1,
    148 : 1,
    165 : 3,
    178 : 1,
    156 : 1,
    145 : 1,
    149 : 1,
    163 : 1,
    162 : 2,
    159 : 2,
    165 : 2,
    180 : 2,
    155 : 2,
    153 : 1,
    152 : 1,
    168 : 2,
    169 : 1
}
tong_hs = 0
for i in ds_thong_ke.values():
    tong_hs += i
print(f"Nhóm có {tong_hs} học sinh!")
ds_cc = []
for j,k in zip(ds_thong_ke.keys(), ds_thong_ke.values()):
    ds_cc.append(j * k)
    print("Chiều cao của hs:", j)
print("Chiều cao trung bình của nhóm học sinh là:", (sum(ds_cc)/tong_hs))