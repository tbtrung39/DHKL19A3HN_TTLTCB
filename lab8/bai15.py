def binh_phuong_so_le():
    n = int(input("Nhap n: "))
    lst = [int(input(f"Nhap so thu {i+1}: ")) for i in range(n)]
    
    ket_qua = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, lst)))
    
    print("Binh phuong cac so le trong list la:", ket_qua)

binh_phuong_so_le()