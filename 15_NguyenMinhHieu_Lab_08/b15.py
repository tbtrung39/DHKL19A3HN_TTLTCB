def nhap_phan_tu():
    n = int(input("Nhập độ dài phần tử: "))
    lst = []
    for i in range(n):
        lst.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))
    return lst
global lst
lst = nhap_phan_tu()
def binh_phuong_so_le():
    binh_phuong_le = list(map(lambda x: x**2, filter(lambda x : x % 2 != 0, lst)))
    return binh_phuong_le
print(binh_phuong_so_le())