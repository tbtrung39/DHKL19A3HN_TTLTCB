lst = []
while(True):
    x = int(input("Nhập phần tử: "))
    if(x == 0):
        break
    lst.append(x)
print(lst)
a = [1, 2, 3]
lst.append(a)
lst.insert(4, a)
lst.insert(0, a)
print("Danh sách sau khi thêm phần tử là:\n", lst)
k = int(input("Nhập vị trí phần tử muốn xoá: "))
while(True):
    if(k <= len(lst)):
        lst.pop(lst[k])
        print(f"Danh sách sau khi xoá phần tử thứ {k} là:\n", lst)
        break
    else:
        print("Nhập lại!")