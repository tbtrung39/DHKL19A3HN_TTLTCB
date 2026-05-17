X = int(input("Nhap X: "))
Y = int(input("Nhap Y: "))
mang = []
for i in range(X):
    hang = []
    for j in range(Y):
        hang.append(i * j)
    mang.append(hang)
print(mang)