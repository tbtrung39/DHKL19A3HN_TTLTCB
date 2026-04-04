s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
i = 0
kq = ""
while i < len(s1) and i < len(s2):
    kq = kq + s1[i] + s2[i]
    i = i + 1
kq = kq + s1[i:] + s2[i:]
print("chuỗi sau khi làm tròn:", kq)