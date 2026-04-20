n = int(input("Nhập số n: "))
key = []
val = []
for i in range(n):
    key.append(int(input(f"Nhập phần tử thứ {i + 1} cần thêm vào: ")))
    val.append(input(f"Nhập tên của khoá thứ {i + 1}: "))
my_dict = dict(zip(key, val))
print(my_dict)