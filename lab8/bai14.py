def tinh_binh_phuong():
    n = int(input("Nhap n: "))
    lst = [int(input(f"Nhap so thu {i+1}: ")) for i in range(n)]
    

    ket_qua = list(map(lambda x: x**2, lst))
    
    print("Danh sach goc:", lst)
    print("Danh sach binh phuong:", ket_qua)


tinh_binh_phuong()