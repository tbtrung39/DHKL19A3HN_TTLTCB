n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    x = int(input("Nhập phần tử thứ " + str(i+1) + ": "))
    a.append(x)

print("Danh sách:", a)

for i in range(len(a)):
    assert a[i] % 2 == 0, "Phần tử " + str(a[i]) + " không phải số chẵn"

print("Tất cả các phần tử đều là số chẵn")
