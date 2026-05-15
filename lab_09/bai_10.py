n = int(input("Nhap n: "))
X_list = [1]
def tinh_X(n):
    if n == 0:
        return 1
    tong = 0
    for i in range(n):
        if i >= len(X_list):
            X_list.append(tinh_X(i))
        tong += ((n - i)**2) * X_list[i]
    return tong
print(f"Gia tri X({n}) la: {tinh_X(n)}")