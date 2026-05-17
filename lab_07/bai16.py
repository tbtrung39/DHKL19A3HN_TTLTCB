a = list(map(int, input("Nhập dãy số (cách nhau bằng dấu cách): ").split()))

pairs = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == a[j]:
            pairs.append((i, j))

print("Dãy a:", a)
print("Các cặp chỉ số (i,j) sao cho a[i] + a[j] = a[j]:")
for pair in pairs:
    print(pair)
