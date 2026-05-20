def tinh_X(n, X=[]):
    if not X:
        X.append(1)  
    if n < len(X):
        return X[n]
    tinh_X(n - 1, X)
    
    tong_Xn = 0
    for i in range(n):
        he_so = (n - i) ** 2
        tong_Xn += he_so * X[i]
    X.append(tong_Xn)
    
    return tong_Xn

if __name__ == "__main__":
    n = int(input("Nhập vào số nguyên dương n: "))
    
    if n < 0:
        print("Vui lòng nhập n >= 0!")
    else:
        mang_luu_tru = []
        ket_qua = tinh_X(n, mang_luu_tru)
        print(f"Giá trị của X_{n} là: {ket_qua}")