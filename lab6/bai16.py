X = int(input("Nhap X hàng: "))
Y = int(input("Nhap Y cột: "))

mang = []
for i in range(X):
    hang = []
    for j in range(Y):
        hang.append(i * j)
    mang.append(hang)

print(mang)