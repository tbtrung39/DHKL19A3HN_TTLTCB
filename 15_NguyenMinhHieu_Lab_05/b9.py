n = int(input("Nhập độ dài danh sách: "))
ds = []
for i in range(n):
    ds.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))
print("Danh sách có được:", ds)
for j in ds:
    assert j % 2 == 0, "{} không phải số chẵn!".format(j)
print("Tất cả đều là số chẵn!")