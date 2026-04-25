import functools as ft
def nhap_so_nguyen():
    lst = []
    while(True):
        i = int(input("Nhập phần tử cho danh sách: "))
        if(i == 0):
            break
        else:
            lst.append(i)
            print("Đã thêm phần tử vào danh sách!")
    return lst
global lst
lst = nhap_so_nguyen()
print(lst)
def tinh_tong_so_chan():
    return ft.reduce(lambda a, b: a + b, filter(lambda x: x % 2 == 0, lst), 0)
print("Tổng các số chẵn trong danh sách đã cho là: ")
print(tinh_tong_so_chan())