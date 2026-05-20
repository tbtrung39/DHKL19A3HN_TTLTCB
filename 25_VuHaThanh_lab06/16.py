X = int(input("Nhập số hàng X: "))
Y = int(input("Nhập số cột Y: "))

mang_2_chieu = []
for i in range(X):
    hang_hien_tai = [] 
    for j in range(Y):
        gia_tri = i * j         
        hang_hien_tai.append(gia_tri) 
    mang_2_chieu.append(hang_hien_tai)
print("Mảng 2 chiều tạo được là:")
print(mang_2_chieu)