from functools import reduce

def tao_danh_sach_tu_1_den_n(n):
    return list(range(1, n + 1))

n = int(input("Nhập n: "))
danh_sach = tao_danh_sach_tu_1_den_n(n)
tong_chan = reduce(lambda a, b: a + b, filter(lambda x: x % 2 == 0, danh_sach), 0)

print(f"Danh sách từ 1 đến {n}: {danh_sach}")
print(f"Tổng các số chẵn: {tong_chan}")
