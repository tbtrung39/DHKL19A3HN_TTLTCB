def nhap_phan_tu():
    while(True):
        n = int(input("Nhập số lượng phần tử: "))
        if(n > 0):
            lst = []
            for i in range(1, n+1):
                lst.append(int(input(f"Nhập phần tủ thứ {i + 1}: ")))
            break
        else:
            print("Số lượng phần tử phải lớn hơn 0!")
    return lst
global lst
lst = nhap_phan_tu()
print(lst)
def list_binh_phuong():
    binh_phuong = list(map(lambda i: i**2, lst))
    return binh_phuong
bp = list_binh_phuong()
print(bp)