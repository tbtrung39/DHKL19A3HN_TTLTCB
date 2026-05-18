n = int(input("Nhập số cần kiểm tra: "))
def find_max(so):
    if(so < 10):
        return so
    else:
        i = so % 10
        con_lai = find_max(so // 10)
        if(con_lai > i):
            return con_lai
        else:
            return i
print(f"Số lớn nhất trong số {n} là: {find_max(n)}")