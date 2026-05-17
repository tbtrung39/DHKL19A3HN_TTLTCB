def tao_danh_sach():
    n = int(input("Nhập số phần tử n: "))
    danh_sach = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        danh_sach.append(x)
    return danh_sach

danh_sach = tao_danh_sach()
danh_sach_binh_phuong = list(map(lambda x: x * x, danh_sach))

print("Danh sách ban đầu:", danh_sach)
print("Danh sách sau khi bình phương:", danh_sach_binh_phuong)
