def max_2_so(a, b):
    if a > b:
        return a
    else:
        return b
def max_3_so(a, b, c):
    return max_2_so(a, max_2_so(b, c))
a = int(input("Nhap so thu 1: "))
b = int(input("Nhap so thu 2: "))
c = int(input("Nhap so thu 3: "))
print("So lon nhat la:", max_3_so(a, b, c))
