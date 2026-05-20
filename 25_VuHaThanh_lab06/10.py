import random

danh_sach_so = [i for i in range(0, 201) if i % 5 == 0 and i % 7 == 0]
so_ngau_nhien = random.choice(danh_sach_so)
print("Danh sách các số thỏa mãn từ 0-200 là:", danh_sach_so)
print("Số ngẫu nhiên chọn được là:", so_ngau_nhien)