n = int(input("Nhap so luong phan tu n: "))
list1 = []
list2 = []

for i in range(n):
    so = int(input(f"Nhap so thu {i+1} cho list1: "))
    list1.append(so)

for i in range(n):
    ten = input(f"Nhap ten thu {i+1} cho list2: ")
    list2.append(ten)

tu_dien = {}
for i in range(n):
    khoa = list1[i]
    gia_tri = list2[i]
    tu_dien[khoa] = gia_tri

print("Noi dung tu dien:")
for k, v in tu_dien.items():
    print(f"{k}:{v}")