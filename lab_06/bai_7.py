List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103],
         ["fri", 115], ["sat", 128], ["sun", 120]]
#1
print("Danh sach:")
for item in List_:
    print(item)

#2
print("Gia tri can lay:", List_[2][1])

#3
print("Do dai:", len(List_))

import random
so = random.randint(1, 200)
phan_tu_moi = ["random", so]
List_.append(phan_tu_moi)
print("Sau khi them:", List_)

#4
tong = 0
for item in List_:
    if item[0] in ["tue", "wed", "sat", "sun"]:
        tong += item[1]
print("Tong can tim:", tong)