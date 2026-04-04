chuoi_a = input("Nhập chuỗi số a (cách nhau bởi dấu phẩy): ")
chuoi_b = input("Nhập chuỗi số b (cách nhau bởi dấu phẩy): ")
chuoi_a = chuoi_a.split(',')
chuoi_b = chuoi_b.split(',')
n = min(len(chuoi_a), len(chuoi_b))
for i in range(n):
    a_i = int(chuoi_a[i].strip())
    b_i = int(chuoi_b[i].strip())
    tong_i = a_i + b_i
    for j in range(i + 1, n):
        a_j = int(chuoi_a[j].strip())
        b_j = int(chuoi_b[j].strip())
        tong_j = a_j + b_j
        if(tong_i == tong_j):
            print(f"{a_i} + {b_i} = {a_j} + {b_j}")
        else:
            print(f"{a_i} + {b_i} != {a_j} + {b_j}")