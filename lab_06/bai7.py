import random
list_ = [["mon", 73],["tue",89],["wed",95],["thu",103],["fri",115],["sat", 128],["sun", 120]]
print("danh sach cac phan tu: ")
for i in list_: 
    print(i)
print("Phan tu can lay: ", list_[2],[1])
ngay = random.choice(["ngay 1","ngay 2","ngay 3","test"])
so = random.randint(10, 20)
list_.append([ngay,so])
print("Danh sach sau khi them: ")
print("list_")
tong = list_[1][1] + list_[2][1] + list_[5][1] + list_[6][1]                                                      
print("Tong sale value: ", tong)