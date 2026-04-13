n = int(input("Nhập độ dài danh sách: "))
ds = []
for i in range(n):
    ds.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))
print("Danh sách ban đầu là:\n", ds)
ds_b = []
choose_num_b = [i for i in ds if(i % 3 == 0 and i % 5 != 0)]
if(choose_num_b):
    ds_b.append(choose_num_b)
    ds_b.sort()
    print("Danh sách B là: \n", ds_b)
else:
    print("Danh sách B trống!")
ds_c = []
binh_phuong = [j**2 for j in ds]
if(binh_phuong):
    ds_c.append(binh_phuong)
    print("Danh sách C là:\n", ds_c)
else:
    print("Danh sách C trống!")
ds_d = []
chia_het_3 = [k for k in ds if(k % 3 == 0)]
if(chia_het_3):
    ds_d.append(chia_het_3)
    print("Danh sách D là:\n", ds_d)
else:
    print("Danh sách D trống!")