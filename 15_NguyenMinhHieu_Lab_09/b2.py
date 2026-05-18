def nhap_so_can_kiem():
    lst = []
    n = int(input("Nhập n số từ bàn phím: "))
    for i in range(1, n + 1):
        lst.append(int(input(f"Nhập phần tử thứ {i}: ")))         
    return lst
lst = nhap_so_can_kiem()
def tim_ucln(x, y):
    if(y == 0):
        return x
    return tim_ucln(y, x % y)
def ucln_lst(lst):
    if(len(lst) == 1):
        return lst[0]
    return tim_ucln(lst[0], ucln_lst(lst[1:]))
print("Ước chung lớn nhất của danh sách các số", lst, "là:")
print(ucln_lst(lst))