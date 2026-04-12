lst = []
while True:
    x = int(input("nhap so(nhap so 0 đe dung):"))
    if x == 0:
        break
    lst.append(x)
print("Danh sach ban dau: ",lst)
#1
lst.insert(0,[1,2,3])  #chèn đầu
lst.append([1,2,3])    #chèn cuối
if len(lst) >= 5:
    lst.insert(4,[1,2,3])   #chèn vào vị trí thứ 5
print("sau khi chèn: ",lst)
#2
k = int(input('nhap vi tri k muon xoa: '))
if 0 <= k < len(lst):
    lst.pop(k)
else:
    print("vi tri k hop le")
print("lst sau khi xoa là: ",lst)

#3 sắp xếp
lst_so = []

for x in lst:
    if type(x) == int:
        lst_so.append(x)
list_tang = sorted(lst_so)
lst_giam = sorted(lst_so,reverse=True)
print("Tang dan: ",list_tang)
print("giam dan: ",lst_giam)