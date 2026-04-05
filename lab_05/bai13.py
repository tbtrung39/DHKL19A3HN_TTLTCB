a = input("Nhap chuoi so A: ")
b = input("Nhap chuoi so B: ")
tim_thay = False
for i in range(1, len(a)):
    c = int(a[:i]) 
    d = int(a[i:])
    for j in range(1, len(b)):
        e = int(b[:j])
        f = int(b[j:])
        if c + d == e + f:
            print(f"Dang thuc dung: {c}+{d} = {e}+{f} (Cung bang {c+d})")
            tim_thay = True
if tim_thay == False:
    print("Khong ton tai cach dat")