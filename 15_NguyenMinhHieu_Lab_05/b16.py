x, y = map(int, input("Nhập x, y: ").split(","))
two_dim_array = []
for i in range(x):
    sub_array = []
    for j in range(y):
        sub_array.append(i*j)
    two_dim_array.append(sub_array)
for k in two_dim_array:
    print(k)