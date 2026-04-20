n = int(input("Nhập độ dài của list: "))
a = []
for i in range(n):
    a.append(int(input("Nhập phần tử cho list: ")))
m = len(a)
kq = []
for j in range(m):
    for k in range(j, m):
        if a[j] + 1 == a[k]:
            kq.append((j, k))
print(f"Các cặp chỉ số (i, j) thỏa mãn: {kq}")