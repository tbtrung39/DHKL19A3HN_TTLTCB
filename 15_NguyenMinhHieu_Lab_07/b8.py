n = int(input("Nhập độ dài của Set: "))
A = set()
for i in range(1, n+1):
    A.add(input(f"Nhập phần tử thứ {i}: "))
print(f"Set A: {A}")
ky_tu_int = 0
ky_tu_str = 0
ky_tu_float = 0
for j in set(A):
    if(j.isdigit()):
        ky_tu_int += 1
    elif(j.isalpha()):
        ky_tu_str += 1
    else:
        ky_tu_float += 1
print("Ký tự dạng chữ:", ky_tu_str)
print("Ký tự dạng số nguyên:", ky_tu_int)
print("Ký tự dạng số thực:", ky_tu_float)