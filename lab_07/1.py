i = 0
set_1 = []
while(True):
    x = input(f"Nhập phần tử thứ {i + 1}: ")
    if(x == "ESC"):
        break
    else:
        set_1.append(x)
        i += 1
A = set(set_1)
print(f"Set ban đầu là:\n {A}")
B = set()
for i in set_1:
    if(not i.isdigit()):
        B.add(i)
print(B)