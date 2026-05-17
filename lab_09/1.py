def max2(a, b):
    if a > b:
        return a
    return b
def max3(a, b, c):
    return max2(max2(a, b), c)


a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print("Số lớn nhất:", max3(a, b, c))