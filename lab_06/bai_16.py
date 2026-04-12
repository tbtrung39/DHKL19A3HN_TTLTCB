X = int(input("Nhap so hang: "))
Y = int(input("Nhap so cot: "))
ma_tran = []
for i in range(X):
    hang = []
    for j in range(Y):
        hang.append(i * j)
    ma_tran.append(hang)
print("Ma tran:")
for hang in ma_tran:
    print(hang)