li = []
while True:
    numbers = int(input("Nhap so (0 de dung): "))
    if numbers == 0: break
    li.append(numbers)
sub = [1, 2, 3]
a = sub + li + sub       
if len(li) >= 5:
    a[4:4] = sub       
print("Sau khi chen list [1,2,3]:", a)
k = int(input("Nhap vi tri k can xoa: "))
if 0 <= k < len(a):
    a.pop(k)
    print(f"Sau khi xoa vi tri {k}:", a)
a.sort()
print("Tang dan:", a)
a.sort(reverse=True)
print("Giam dan:", a)